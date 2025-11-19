#!/usr/bin/env python3
"""
Stub generator script for the Raysect library.

This script analyzes the installed Raysect library and generates
type stub files (.pyi) for all public modules and classes by
introspecting the loaded modules without reading source code.
"""

import argparse
import importlib
import inspect
import pkgutil
import sys
from pathlib import Path
from typing import Any

# Dunder methods actually defined in Raysect source code (.pyx/.pxd files)
# Categorized by functionality - order preserved for stub generation
COMMON_DUNDER_METHODS_ORDERED = [
    # Object construction and destruction
    "__init__",  # Object initialization
    "__cinit__",  # Cython constructor
    "__dealloc__",  # Cython destructor
    # String representation and conversion
    "__repr__",  # Developer string representation
    "__str__",  # User string representation
    # Arithmetic operations (binary)
    "__add__",  # Addition: a + b
    "__radd__",  # Right addition: b + a
    "__sub__",  # Subtraction: a - b
    "__rsub__",  # Right subtraction: b - a
    "__mul__",  # Multiplication: a * b
    "__rmul__",  # Right multiplication: b * a
    "__truediv__",  # True division: a / b
    "__rtruediv__",  # Right true division: b / a
    "__mod__",  # Modulo: a % b
    "__rmod__",  # Right modulo: b % a
    "__pow__",  # Power: a ** b
    "__rpow__",  # Right power: b ** a
    # Arithmetic operations (unary)
    "__neg__",  # Unary negation: -a
    "__abs__",  # Absolute value: abs(a)
    # Comparison operations
    "__richcmp__",  # Cython rich comparison method
    "__eq__",  # Equality: a == b
    "__ne__",  # Inequality: a != b
    "__lt__",  # Less than: a < b
    "__le__",  # Less or equal: a <= b
    "__gt__",  # Greater than: a > b
    "__ge__",  # Greater or equal: a >= b
    # Sequence/container protocols
    "__getitem__",  # Item access: a[key]
    "__setitem__",  # Item assignment: a[key] = value
    "__iter__",  # Iteration: for x in a
    "__len__",  # Length: len(a)
    # Callable protocol
    "__call__",  # Function call: a()
    # Serialization support (pickling)
    "__getstate__",  # Get object state for pickling
    "__setstate__",  # Restore object state from pickling
    "__reduce__",  # Reduce for pickling
]

# Create a set for quick lookup
COMMON_DUNDER_METHODS_SET = set(COMMON_DUNDER_METHODS_ORDERED)


def main():
    """Main entry point for stub generation."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Generate type stubs for the Raysect library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s                    # Generate new files only (default)
  %(prog)s --overwrite        # Overwrite existing files
  %(prog)s -o output/dir      # Specify output directory
  %(prog)s --overwrite -o .   # Overwrite in current directory""",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing .pyi files (default: only create new files)")
    parser.add_argument("-o", "--output", type=Path, default=Path("src/raysect-stubs"), help="Output directory for stub files (default: src/raysect-stubs)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    print("Raysect Stub Generator")
    print("=====================")

    # Check if raysect is available
    try:
        import raysect

        print(f"Found Raysect version: {getattr(raysect, '__version__', 'unknown')}")
    except ImportError:
        print("Error: Raysect library not found. Please install it first.")
        sys.exit(1)

    # Create output directory
    stub_dir = args.output
    stub_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating stubs in: {stub_dir}")
    print(f"Overwrite mode: {'enabled' if args.overwrite else 'disabled (new files only)'}")
    if args.verbose:
        print("Verbose mode enabled")
    print("Scanning modules and extracting classes/functions...")

    # Discover all modules (excluding tests)
    modules = discover_modules()

    # Generate stubs for each module
    generated_count = 0
    skipped_count = 0
    for module_name in modules:
        result = generate_module_stub(module_name, stub_dir, args.overwrite, args.verbose)
        if result == "generated":
            generated_count += 1
        elif result == "skipped":
            skipped_count += 1

    print("\nStub generation complete!")
    print(f"Generated: {generated_count} stub files")
    if skipped_count > 0:
        print(f"Skipped: {skipped_count} existing files (use --overwrite to replace)")
    print("Note: Type annotations may need manual refinement.")


def discover_modules() -> list[str]:
    """Discover all non-test modules in raysect package."""
    import raysect

    modules = []
    # Always include the main module
    modules.append("raysect")

    # Walk through all submodules
    for _, modname, _ in pkgutil.walk_packages(raysect.__path__, raysect.__name__ + "."):
        # Skip test modules/packages
        if ".test" in modname or modname.endswith(".tests"):
            continue
        modules.append(modname)

    return sorted(modules)


def generate_module_stub(module_name: str, stub_dir: Path, overwrite: bool = False, verbose: bool = False) -> str:
    """Generate stub file for a specific module.

    Returns:
        "generated" if file was created/overwritten
        "skipped" if file exists and overwrite is False
        "failed" if generation failed
    """
    try:
        # Import the module
        module = importlib.import_module(module_name)

        # Create directory structure
        if module_name == "raysect":
            stub_file = stub_dir / "__init__.pyi"
            stub_file.parent.mkdir(parents=True, exist_ok=True)
        else:
            # Convert module name to path (e.g., raysect.core.math -> raysect-stubs/core/math)
            relative_path = module_name.replace("raysect.", "").replace(".", "/")
            if hasattr(module, "__path__"):  # It's a package
                stub_file = stub_dir / relative_path / "__init__.pyi"
            else:  # It's a module
                stub_file = stub_dir / f"{relative_path}.pyi"
            stub_file.parent.mkdir(parents=True, exist_ok=True)

        # Check if file exists and handle overwrite logic
        if stub_file.exists() and not overwrite:
            if verbose:
                print(f"  Skipped (exists): {stub_file}")
            return "skipped"

        # Generate stub content
        content = generate_stub_content(module, module_name)

        # Write stub file
        stub_file.write_text(content)
        action = "Overwritten" if stub_file.exists() and overwrite else "Generated"
        print(f"  {action}: {stub_file}")
        return "generated"

    except Exception as e:
        print(f"  Warning: Failed to process {module_name}: {e}")
        return "failed"


def generate_stub_content(module: Any, module_name: str) -> str:
    """Generate stub content for a module."""
    lines = [
        f'"""Type stubs for {module_name}"""',
        "",
    ]

    # Get module docstring if available
    if hasattr(module, "__doc__") and module.__doc__:
        # Add first line of docstring as comment
        first_line = module.__doc__.strip().split("\n")[0]
        if first_line:
            lines.append(f"# {first_line}")
            lines.append("")

    # Collect imports needed
    imports = set()

    # Get all public members
    members = get_public_members(module)

    # Process classes
    classes = []
    for name, obj in members.get("classes", []):
        if obj.__module__ == module_name:
            class_stub = generate_class_stub(obj, name, imports)
            classes.append(class_stub)

    # Process functions
    functions = []
    for name, obj in members.get("functions", []):
        if obj.__module__ == module_name:
            func_stub = generate_function_stub(obj, name, imports)
            functions.append(func_stub)

    # Process constants and variables
    constants = []
    for name, obj in members.get("constants", []):
        const_stub = generate_constant_stub(name, obj, imports)
        constants.append(const_stub)

    # Add common imports if we have content
    if classes or functions or constants:
        lines.append("from typing import Any")
        lines.append("")

    # Add constants
    if constants:
        lines.extend(constants)
        lines.append("")

    # Add functions
    if functions:
        lines.extend(functions)
        lines.append("")

    # Add classes
    if classes:
        lines.extend(classes)

    # If nothing was found, add a placeholder
    if not classes and not functions and not constants:
        lines.append("# No public API detected - may need manual inspection")

    return "\n".join(lines)


def get_public_members(module: Any) -> dict[str, list]:
    """Extract public members from a module."""
    classes = []
    functions = []
    constants = []

    for name, obj in inspect.getmembers(module):
        # Skip private members
        if name.startswith("_"):
            continue

        if inspect.isclass(obj):
            classes.append((name, obj))
        elif inspect.isfunction(obj) or inspect.isbuiltin(obj) or callable(obj):
            # Include Cython functions and other callables
            functions.append((name, obj))
        elif not inspect.ismodule(obj):
            # Treat as constant/variable
            constants.append((name, obj))

    return {"classes": classes, "functions": functions, "constants": constants}


def generate_class_stub(cls: Any, class_name: str, imports: set[str]) -> str:
    """Generate stub for a class."""
    lines = [f"class {class_name}:"]

    # Add docstring if available
    if hasattr(cls, "__doc__") and cls.__doc__:
        first_line = cls.__doc__.strip().split("\n")[0]
        if first_line:
            lines.append(f'    """{first_line}"""')

    # Get class methods and properties
    methods = []
    properties = []

    # Get methods defined directly in the class dict (not inherited)
    class_dict_methods = set()
    if hasattr(cls, "__dict__"):
        class_dict_methods = set(cls.__dict__.keys())

    for name, member in inspect.getmembers(cls):
        # Include dunder methods (like __getitem__, __add__, etc.) but exclude most private methods
        if name.startswith("_") and not (name.startswith("__") and name.endswith("__")):
            continue

        if callable(member) and not inspect.isdatadescriptor(member):
            # For dunder methods, be more selective - only include common ones that are likely user-defined
            if name.startswith("__") and name.endswith("__"):
                # Use global definition of dunder methods
                if name in COMMON_DUNDER_METHODS_SET and name in class_dict_methods:
                    method_stub = generate_method_stub(member, name, imports)
                    methods.append(method_stub)
            # For non-dunder methods, include if they're defined in this class or module
            else:
                should_include = False
                # Check if method is in class dict (defined directly in class)
                if name in class_dict_methods:
                    should_include = True
                # For Cython methods, check module match
                elif hasattr(member, "__module__") and member.__module__ == cls.__module__:
                    should_include = True

                if should_include:
                    method_stub = generate_method_stub(member, name, imports)
                    methods.append(method_stub)
        elif inspect.isdatadescriptor(member) and not name.startswith("_"):
            prop_stub = f"    {name}: Any"
            properties.append(prop_stub)

    # Add properties
    if properties:
        lines.extend(properties)
        lines.append("")

    # Add methods (sorted by dunder method order, then regular methods)
    if methods:
        # Use global ordered list for sorting
        def method_sort_key(method_line):
            # Extract method name from the line (e.g., "    def __init__(..." -> "__init__")
            method_name = method_line.strip().split("(")[0].split()[-1]

            if method_name in COMMON_DUNDER_METHODS_ORDERED:
                return (0, COMMON_DUNDER_METHODS_ORDERED.index(method_name))  # Dunder methods in defined order
            elif method_name.startswith("__") and method_name.endswith("__"):
                return (1, method_name)  # Other dunder methods (alphabetical)
            else:
                return (2, method_name)  # Regular methods (alphabetical)

        methods.sort(key=method_sort_key)
        lines.extend(methods)

    # If no methods found, add pass
    if not methods and not properties:
        lines.append("    ...")

    lines.append("")
    return "\n".join(lines)


def generate_method_stub(method: Any, method_name: str, imports: set[str]) -> str:
    """Generate stub for a method."""
    try:
        # Try to get signature
        sig = inspect.signature(method)
        params = []

        for param_name, param in sig.parameters.items():
            if param.annotation != param.empty:
                # Has annotation - try to use it
                params.append(f"{param_name}: Any")  # Simplified for now
            else:
                params.append(param_name)

        params_str = ", ".join(params)
        return_annotation = " -> Any" if sig.return_annotation != sig.empty else ""

        return f"    def {method_name}({params_str}){return_annotation}: ..."

    except (ValueError, TypeError):
        # Fallback for built-in methods or methods without signature
        if method_name == "__init__":
            return f"    def {method_name}(self, *args: Any, **kwargs: Any) -> None: ..."
        else:
            return f"    def {method_name}(self, *args: Any, **kwargs: Any) -> Any: ..."


def generate_function_stub(func: Any, func_name: str, imports: set[str]) -> str:
    """Generate stub for a function."""
    try:
        sig = inspect.signature(func)
        params = []

        for param_name, param in sig.parameters.items():
            if param.annotation != param.empty:
                params.append(f"{param_name}: Any")  # Simplified
            else:
                params.append(param_name)

        params_str = ", ".join(params)
        return_annotation = " -> Any" if sig.return_annotation != sig.empty else ""

        return f"def {func_name}({params_str}){return_annotation}: ..."

    except (ValueError, TypeError):
        # Fallback for built-in functions
        return f"def {func_name}(*args: Any, **kwargs: Any) -> Any: ..."


def generate_constant_stub(name: str, obj: Any, imports: set[str]) -> str:
    """Generate stub for a constant."""
    # Try to infer type from value
    if isinstance(obj, (int, float)):
        type_name = type(obj).__name__
    elif isinstance(obj, str):
        type_name = "str"
    elif isinstance(obj, bool):
        type_name = "bool"
    else:
        type_name = "Any"
        imports.add("Any")

    return f"{name}: {type_name}"


if __name__ == "__main__":
    main()

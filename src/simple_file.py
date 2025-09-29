# test_environment.py

import sys
import platform

print("=== Python Environment Test Routine ===")
print("---------------------------------------")

# Test 1: Python Version
print(f"✅ Python Version: {sys.version}")

# Test 2: Platform
print(f"✅ Operating System: {platform.system()} {platform.release()} ({platform.machine()})")

# Test 3: Common Libraries
print("\n=== Testing Common Libraries ===")
libraries_to_test = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "sklearn",
    "pytest"
]

for lib in libraries_to_test:
    try:
        __import__(lib)
        print(f"✅ {lib}: Successfully imported.")
    except ImportError:
        print(f"❌ {lib}: Not found. Please install with 'pip install {lib}'.")
    except Exception as e:
        print(f"⚠️ {lib}: An error occurred: {e}")

print("\n---------------------------------------")
print("Test completed. All checks marked with ✅ are successful.")
print("If any test failed, please check the error message for details.")
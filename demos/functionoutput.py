import inspect
import sltfluxpy

for name, obj in inspect.getmembers(sltfluxpy, inspect.isfunction):
    print(f"{name}{inspect.signature(obj)}  ")
import json

cpu_repository = json.load(open('../../../database/cpu.json'))

# Find CPU by model name, or thrown a StopIteration exception if not found.
def find_cpu_by_name(name: str):
    return next(item for item in cpu_repository['list'] if item['name'] == name)

# Find CPU by model codename, or thrown a StopIteration exception if not found.
def find_cpu_by_codename(codename: str):
    return next(item for item in cpu_repository['list'] if item['codename'] == codename)


from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
nbs=sorted((root/'notebooks').glob('*.ipynb'))
issues=[]
for p in nbs:
    nb=json.loads(p.read_text(encoding='utf-8'))
    for i,c in enumerate(nb['cells']):
        if c['cell_type']=='code':
            if c.get('outputs'): issues.append(f'{p.name} cell {i}: outputs not empty')
            if c.get('execution_count') is not None:issues.append(f'{p.name} cell {i}: execution count not empty')
        src=''.join(c.get('source',[]))
        if re.search(r'(?i)(?:api[_-]?key|access[_-]?token|password)\s*=\s*["\'][^"\']{10,}["\']',src):
            issues.append(f'{p.name} cell {i}: potential hardcoded secret')
print(f'Validated {len(nbs)} notebook JSON files and cleaned outputs.')
if issues:
    print('\n'.join(issues));sys.exit(1)
print('PASS: static source-release checks. This does not verify full data-dependent reproducibility.')

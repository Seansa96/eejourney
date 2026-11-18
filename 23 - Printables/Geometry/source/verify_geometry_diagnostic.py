"""Independent numerical/structural checks plus full PDF rendering for visual QA."""
from pathlib import Path
import importlib.util, math, json, collections, sys
import fitz
from PIL import Image, ImageDraw

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('geometry',HERE/'build_geometry_diagnostic.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
mod.validate_data()

def eq(a,b): assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-10),(a,b)
def dist(a,b):return math.hypot(a[0]-b[0],a[1]-b[1])

# Recompute the numeric answers using separate representations where useful.
x=(6+2)/(3-1);eq(2*(3*x-2),20);eq(3*x-2+3,13);eq(x+6-3,7) # Q1
eq(180-64,116) # Q2
eq(abs((-90)-(28-90)),28) # Q3 directions
mid=((-2+6)/2,(1+1)/2);p=(mid[0],mid[0]+1)
assert p==(2,3);eq(dist(p,(-2,1)),2*math.sqrt(5));eq(dist(p,(-2,1)),dist(p,(6,1))) # Q4
assert sum([37,143,37,143])==360 # Q5
eq((180-38)/2,71);eq(180-71,109) # Q6
eq(360/(180-150),12);eq((12-2)*180,12*150);assert 12-3==9 # Q7
eq(180-68/2-(180-68)/2,90) # Q8
base=(180-36)/2;inner=180-2*base;eq(inner,36);eq(base-inner,36) # Q9
assert [n for n in range(1,20) if 5+n>8 and 8+n>5 and 5+8>n]==list(range(4,13)) # Q10
eq(math.hypot(6,8),10);eq(6*8/10,24/5) # Q11
# Q12: genuinely ambiguous SSA example, via ray/circle intersection, not sine law.
eq(math.hypot(6,8),10) # primary SAS configuration is also metrically consistent
foot=9*math.cos(math.radians(50));alt=9*math.sin(math.radians(50))
assert alt<7<9;root=math.sqrt(7**2-alt**2);assert 0<foot-root<foot+root
eq(dist((9*math.cos(math.radians(50)),9*math.sin(math.radians(50))),(foot-root,0)),7)
eq(8/(6/9)-8,4);eq(12*(6/9),8);eq((6/9)**2,4/9) # Q13
eq(12*math.sin(math.pi/6),6);eq(12*math.cos(math.pi/6),6*math.sqrt(3));eq(math.hypot(3,3),3*math.sqrt(2)) # Q14
# Q15 solve the simultaneous Pythagorean equations for the height, then both legs.
h2=(13**2-4**2-9**2)/2;eq(h2,36);eq(4**2+h2,52);eq(9**2+h2,117);eq(52+117,169)
eq(124/2,62);eq((360-124)/2,118) # Q16
eq(13**2-5**2,12**2);eq((13-5)*(13+5),144) # Q17
eq(3*8/4,6);eq((80+120)/2,100) # Q18 independent circles
x=(180-4)/8;eq(x,22);eq(3*x+10,76);eq(5*x-6,104);eq(180-110,70) # Q19
eq(math.sqrt(10**2-6**2),8);eq(10*2*math.asin(.6),20*math.asin(.6)) # Q20
eq(12*9-4*3,96);eq(12+6+4+3+8+9,42) # Q21
eq(4*(.5*5*12),120);eq(math.hypot(5,12),13);eq(13*8,104) # Q22
eq((120/360)*36,12);eq(.5*(6*math.sqrt(3))*3,9*math.sqrt(3)) # Q23 coefficients of π and √3
eq(45/(1-(2/3)**2),81);eq(81*(2/3)**2,36);eq((math.sqrt(2)/2)**2,.5) # Q24
eq(.5*6*8*10,240);eq(3**2*5,45) # Q25 π coefficient
eq(3**2*8+3**2*4/3,84);eq(84*2**3,672) # Q26 π coefficient
eq(10**3,1000);eq(2**2*10,40);eq((4/3)*(5**3-3**3),392/3) # Q27
eq(8*5+2*8*3+2*5*3,118);eq(8*5,40) # Q28
eq(2*3*10,60);eq(2*3*10+2*3**2,78);eq(2*3*10+3**2,69);eq(4*3**2,36) # Q29 π coefficients
slant=math.hypot(3,4);eq(slant,5);eq(2*3*8+3*slant+3**2,72);eq(72*3**2,648) # Q30 π coefficients

# Confirm glyph coverage, rather than relying only on text extraction.
for q in mod.QUESTIONS:
 text=json.dumps(q,ensure_ascii=False)
 for ch in text:
  if ch.isspace():continue
  font='Math' if ch in '∠∥⟂' else 'Body'
  assert ord(ch) in mod.pdfmetrics.getFont(font).face.charToGlyph,(q['n'],ch)

summary={"items":30,"points":300,"difficulty":dict(collections.Counter(q['level'] for q in mod.QUESTIONS)),"numerical_checks":"passed","pdfs":[]}
for path in sorted(HERE.parent.glob('*.pdf')):
 doc=fitz.open(path);stem='grader' if 'Solutions' in path.name else 'student'
 assert len(doc)==(40 if stem=='grader' else 32)
 alltext='\n'.join(p.get_text() for p in doc)
 assert '\ufffd' not in alltext and '\x00' not in alltext
 if stem=='student':
  assert 'Worked solution' not in alltext and 'Analytic rubric' not in alltext
  for q in mod.QUESTIONS:
   page=doc[q['n']+1]
   assert q['title'] in page.get_text()
   assert 'Work and explanation:' in page.get_text()
   assert 'Confidence' in page.get_text()
   long_horizontal=sum(1 for d in page.get_drawings() if d['rect'].width>520 and d['rect'].height<1)
   assert long_horizontal>=9,(q['n'],long_horizontal)
  assert '∠' in alltext and '∥' in alltext
 else:
  assert alltext.count('Analytic rubric')==30
  assert alltext.count('Worked solution')==30
 for i,page in enumerate(doc):
  for block in page.get_text('dict')['blocks']:
   if 'lines' not in block:continue
   for line in block['lines']:
    for span in line['spans']:
     x0,y0,x1,y1=span['bbox']
     assert 39<=x0<x1<=573 and 12<=y0<y1<=775,(stem,i+1,span['text'],span['bbox'])
  for span in page.get_texttrace():
   for codepoint,glyph,*rest in span['chars']:
    assert glyph!=0,(stem,i+1,chr(codepoint))
  page.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(mod.QA/f'{stem}-{i+1:02}.png')
 for start in range(0,len(doc),8):
  sheet=Image.new('RGB',(1600,1080),'#cdd4d9');draw=ImageDraw.Draw(sheet)
  for j in range(min(8,len(doc)-start)):
   im=Image.open(mod.QA/f'{stem}-{start+j+1:02}.png');im.thumbnail((388,510))
   x=(j%4)*400+(400-im.width)//2;y=(j//4)*540+22
   sheet.paste(im,(x,y));draw.text((x,y-16),f'{stem} {start+j+1}',fill='black')
  sheet.save(mod.QA/f'{stem}-contact-{start//8+1}.png')
 summary['pdfs'].append({'file':path.name,'pages':len(doc),'bytes':path.stat().st_size,'text_boundaries':'passed','glyphs':'passed','rendered_pages':len(doc)})
assert len(summary['pdfs'])==2
(HERE/'validation_report.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))

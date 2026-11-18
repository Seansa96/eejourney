"""Rebuild the two PDFs with Python 3, ReportLab and PyMuPDF.
Run from any directory. See README.md for installation and validation.
All assessment questions and diagrams are original; sources are topic alignments.
"""
from pathlib import Path
import sys, math, json, collections, re
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'tmp' / 'geometry-diagnostic-deps'))
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = Path(__file__).resolve().parents[1]
QA = ROOT / 'tmp' / 'geometry-review'
QA.mkdir(parents=True, exist_ok=True)
FONTDIR = Path('C:/Windows/Fonts')
for name, filename in [('Body','arial.ttf'),('Bold','arialbd.ttf'),('Italic','ariali.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONTDIR / filename)))
pdfmetrics.registerFont(TTFont('Math', str(FONTDIR / 'seguisym.ttf')))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
INK = colors.HexColor('#172938'); ACCENT = colors.HexColor('#245d69')
GRAY = colors.HexColor('#52626c'); LIGHT = colors.HexColor('#dce3e6')
W,H = 612,792
QUESTIONS=[]

def item(topic, level, title, stem, parts, solution, rubric, refs, errors, diagram=None):
    # parts = (label, point total, prompt); rubric = (part, points, skill, observable evidence)
    q=dict(n=len(QUESTIONS)+1,topic=topic,level=level,title=title,stem=stem,
           parts=parts,solution=solution,rubric=rubric,refs=refs,errors=errors,diagram=diagram)
    QUESTIONS.append(q)

item('Lines','F','Segments and midpoints',
 'Points A, M, and B lie on one straight line in that order. M is the midpoint of AB. AM = 3x − 2 cm and MB = x + 6 cm.',
 [('a',6,'Find x and the length AB. Explain the equation you use.'),('b',4,'A point N lies on segment MB and MN = 3 cm. Find AN and NB. Label the point order on a sketch.')],
 [('a','Midpoint means AM = MB, so 3x − 2 = x + 6, giving x = 4. AM = MB = 10 cm and AB = 20 cm.'),('b','The order is A–M–N–B. AN = AM + MN = 10 + 3 = 13 cm; NB = MB − MN = 10 − 3 = 7 cm. The lengths total 20 cm.')],
 [('a',2,'midpoint','Equates the two half-segments.'),('a',2,'linear algebra','Solves x = 4.'),('a',2,'segment addition','Finds AB = 20 cm.'),('b',1,'point order','Shows A–M–N–B.'),('b',3,'segment addition','AN = 13 cm (1), NB = 7 cm (1), valid addition/subtraction with units (1).')],
 ['A10.1'], 'Adding the expressions without using the midpoint; placing N outside MB.', 'segments')

item('Lines','F','Parallel lines and a transversal',
 'In the diagram, lines ℓ and m are parallel. A transversal crosses ℓ at P and m at Q. The marked angle at P is 64°. Angles α and β are the sectors indicated at Q.',
 [('a',6,'Find α and β, naming a geometric relationship for each.'),('b',4,'Explain whether knowing the marked 64° angle alone would determine α if the parallel-line condition were removed.')],
 [('a','α = 64° by corresponding angles. β = 180° − 64° = 116° by a linear pair (or same-side interior relationships).'),('b','No. Without parallelism the lower line can rotate about Q while the upper configuration stays fixed; α can change. The parallel-line hypothesis is essential.')],
 [('a',3,'corresponding angles','α = 64° (1); identifies corresponding positions and parallelism (2).'),('a',3,'supplementary angles','β = 116° (1); uses a 180° linear pair correctly (2).'),('b',4,'necessary hypotheses','Says not determined (1) and explains a possible rotation/counterconfiguration (3).')],
 ['A10.3','Z8.2'], 'Treating angles as equal because the drawing looks parallel; confusing adjacent and corresponding sectors.', 'parallel')

item('Lines','S','Perpendicular directions',
 'A straight ramp rises to the right at 28° above a horizontal line. A vertical line points downward from a point on the ramp. A second ray at that point is perpendicular to the ramp and points downward and to the right.',
 [('a',4,'Draw and label the configuration, including both perpendicular relationships.'),('b',6,'Find the smaller angle between the downward vertical ray and the downward-right perpendicular ray. Explain without measuring your sketch.')],
 [('a','Draw the ramp up-right, the horizontal right, the vertical down, and the ramp-normal down-right. Vertical is perpendicular to horizontal; the second ray is perpendicular to the ramp.'),('b','The ramp makes 62° with the upward vertical. Its perpendicular points 62° below the rightward horizontal, while downward vertical is 90° below horizontal. The difference is 28°. Equivalently, rotating both horizontal and ramp by 90° preserves their 28° angle.')],
 [('a',2,'direction interpretation','Correctly orients the two specified rays.'),('a',2,'perpendicularity','Marks vertical/horizontal and ramp/normal right angles.'),('b',4,'complementary angles','Derives the 28° angle from 90° complements or a common rotation.'),('b',2,'angle selection','Reports the smaller angle 28°, not 62° or 152°.')],
 ['A10.3','Z8.2','T'], 'Using the complementary angle or reversing one ray.', None)

item('Lines','A','Equal-distance locations',
 'On a coordinate plane, A = (−2, 1) and B = (6, 1). A point P is equally far from A and B and also lies on the line y = x + 1.',
 [('a',4,'Describe the entire line of points equally far from A and B. Explain its location and direction.'),('b',6,'Find P and its exact distance from A. Explain how the two conditions locate P uniquely.')],
 [('a','The midpoint of AB is (2,1). AB is horizontal, so its perpendicular bisector is x = 2. Every point on that line is equally far from A and B; points off it are not.'),('b','Intersect x = 2 with y = x + 1 to get P = (2,3). PA = √((2 + 2)² + (3 − 1)²) = √20 = 2√5. The vertical line meets the nonvertical line once. An alternative is to equate squared distances, obtain x = 2, and substitute.')],
 [('a',2,'midpoint','Finds midpoint (2,1).'),('a',2,'perpendicular bisector','Identifies and explains x = 2.'),('b',2,'line intersection','Finds P = (2,3).'),('b',3,'distance','Correct displacement (1), squared-distance computation (1), exact 2√5 (1).'),('b',1,'uniqueness','Explains a single intersection.')],
 ['A10.1','A16','Z8.2'], 'Choosing the midpoint as P without checking the other condition; confusing x = 2 and y = 2.', None)

item('Angle chasing','F','Crossing lines',
 'Two full straight lines AB and CD intersect at O. A and B are opposite each other across O, as are C and D. Angle AOC is 37°.',
 [('a',6,'Find angles COB, BOD, and DOA. Draw and label all four sectors.'),('b',4,'Explain which angles are vertical and which relationship gives the adjacent angles. Check the sum around O.')],
 [('a','∠COB = 143°, ∠BOD = 37°, and ∠DOA = 143°.'),('b','AOC and BOD are vertical, as are COB and DOA. Adjacent sectors form linear pairs summing to 180°. The four angles sum to 37 + 143 + 37 + 143 = 360°.')],
 [('a',3,'angle calculation','One point for each correct angle.'),('a',3,'sector interpretation','A correctly labeled crossing sketch with opposite rays and corresponding sectors.'),('b',2,'angle relationships','Vertical equality (1), linear-pair supplement (1).'),('b',2,'checking','Shows a correct 360° sum.')],
 ['A10.2','Z8.2'], 'Calling adjacent angles vertical; making all four equal.', None)

item('Angle chasing','F','Isosceles triangle and extension',
 'Triangle ABC has AB = AC and ∠BAC = 38°. Side BC is extended through C to D.',
 [('a',6,'Find ∠ABC and ∠ACB. State why they are equal.'),('b',4,'Find exterior angle ACD and explain its relationship to the interior angles.')],
 [('a','The equal sides give equal base angles. Each is (180° − 38°)/2 = 71°.'),('b','∠ACD = 180° − 71° = 109°. It also equals the two remote interior angles, 38° + 71°.')],
 [('a',2,'isosceles structure','Connects equal sides to equal opposite angles.'),('a',4,'triangle angle sum','Subtracts 38° from 180° (2), divides equally and gives both 71° (2).'),('b',2,'exterior angle','Obtains 109°.'),('b',2,'justification','Uses a straight angle or the remote-interior sum.')],
 ['A11.1','Z8.2'], 'Putting equal angles at the endpoints of the unequal side incorrectly; forgetting the extension direction.', 'isosceles')

item('Angle chasing','S','A polygon from its angles',
 'Every interior angle of a convex regular polygon measures 150°.',
 [('a',6,'Find the number of sides, showing the angle relationship you use.'),('b',4,'Find the number of diagonals drawn from one vertex, and explain how the triangles formed from that vertex check your answer in part (a).')],
 [('a','The exterior turning angle is 180° − 150° = 30°. A full turn is 360°, so n = 360/30 = 12. Alternatively solve 150n = 180(n − 2).'),('b','There are n − 3 = 9 diagonals from one vertex and n − 2 = 10 triangles. Their angle sum is 10(180°) = 1800°, equal to 12(150°).')],
 [('a',3,'polygon relationship','Sets up exterior-turn or interior-sum equation.'),('a',3,'side count','Obtains 12 with valid calculation.'),('b',2,'diagonals','Finds 9, excluding the vertex itself and its two neighbors.'),('b',2,'triangulation check','Uses 10 triangles to check 1800°.')],
 ['A13.2','A13.3'], 'Using 360/150; confusing diagonals with triangles.', None)

item('Angle chasing','S','Bisectors in a parallelogram',
 'ABCD is a convex parallelogram with vertices named in order and ∠DAB = 68°. The internal angle bisectors at A and B meet at P inside the parallelogram.',
 [('a',4,'Find ∠ABC, ∠BAP, and ∠ABP.'),('b',6,'Find ∠APB. Explain why the angle between these two adjacent internal bisectors would have the same measure in any such parallelogram where they meet.')],
 [('a','Adjacent parallelogram angles are supplementary: ∠ABC = 112°. Bisecting gives ∠BAP = 34° and ∠ABP = 56°.'),('b','In triangle ABP, ∠APB = 180° − 34° − 56° = 90°. In general the original adjacent angles sum to 180°, so their halves sum to 90°, leaving 90° at the intersection.')],
 [('a',2,'parallel-line angles','Finds 112° using supplementary adjacent angles.'),('a',2,'angle bisectors','Finds 34° and 56° (1 each).'),('b',2,'triangle angle sum','Obtains 90°.'),('b',4,'generalization','Explains half of a supplementary sum is 90° (2), so the remaining triangle angle is 90° regardless of initial angle (2).')],
 ['A12.3','A14','Z8.2'], 'Treating the bisectors as equal lengths or halving an angle at the wrong vertex.', 'bisectors')

item('Angle chasing','A','A hidden bisector',
 'Triangle ABC has AB = AC and ∠BAC = 36°. Point D is strictly between A and C and satisfies BD = BC.',
 [('a',4,'Find ∠ABC, ∠BCD, and ∠BDC, giving the reasons.'),('b',6,'Find ∠ABD and ∠DBC. Decide whether BD bisects ∠ABC and explain using the angles you found.')],
 [('a','The base angles of ABC are 72°. Since D lies on AC, ∠BCD = ∠BCA = 72°. In BCD, BD = BC, so the opposite angles BCD and BDC are equal: ∠BDC = 72°.'),('b','The remaining angle DBC is 180° − 72° − 72° = 36°. Thus ∠ABD = 72° − 36° = 36°, so BD does bisect ∠ABC. This conclusion follows from the length condition, not from how the drawing looks.')],
 [('a',2,'outer isosceles triangle','Finds base angles 72° with explanation.'),('a',2,'inner isosceles triangle','Transfers BCD = 72° and gets BDC = 72° with correct opposite-side reasoning.'),('b',2,'nested angle sum','Finds DBC = 36°.'),('b',2,'angle subtraction','Finds ABD = 36°.'),('b',2,'inferred bisector','Concludes bisector from the two equal angle measures.')],
 ['A14','Z8.2'], 'Assuming D is a midpoint or BD a bisector before establishing it; reversing equal-side opposite angles.', 'hidden')

item('Triangles','F','Which lengths form a triangle?',
 'Two sides of a nondegenerate triangle have lengths 5 cm and 8 cm. The third side has length x cm.',
 [('a',6,'Find the complete range of possible real values of x and explain both endpoints.'),('b',4,'If x must be an integer, how many values are possible? Give an example at an excluded endpoint and explain why it fails.')],
 [('a','Triangle inequality gives |8 − 5| < x < 8 + 5, so 3 < x < 13. At 3 the shorter segments just span the longest; at 13 the two given sides just span the third. Equality produces a flat, degenerate configuration.'),('b','Integers 4 through 12 give 9 possibilities. Either 3 or 13 is excluded because equality collapses the triangle onto a line.')],
 [('a',2,'triangle inequality','Lower strict bound x > 3.'),('a',2,'triangle inequality','Upper strict bound x < 13.'),('a',2,'degeneracy','Explains why endpoints are excluded.'),('b',2,'integer range','Lists/describes 4 through 12 and counts 9.'),('b',2,'boundary example','Gives an endpoint and explains collinearity.')],
 ['A11.3'], 'Allowing equality; supplying only the upper bound.', None)

item('Triangles','F','A right triangle and its height',
 'Triangle ABC is right-angled at C. AC = 6 cm and BC = 8 cm.',
 [('a',5,'Find AB exactly and identify why it is the hypotenuse.'),('b',5,'Find the altitude from C to AB. Use a labeled sketch and explain how you obtain it.')],
 [('a','AB is opposite the right angle; AB² = 6² + 8² = 100, so AB = 10 cm.'),('b','Area = (1/2)(6)(8) = 24 cm². Using AB as base gives 24 = (1/2)(10)h, hence h = 24/5 cm. A similarity derivation is equally valid.')],
 [('a',1,'hypotenuse','Identifies AB as opposite C.'),('a',2,'Pythagorean theorem','Sets up AB² = 6² + 8².'),('a',2,'exact length','Finds 10 cm.'),('b',2,'area relationship','Computes 24 cm².'),('b',2,'altitude','Sets up and solves h = 24/5 cm.'),('b',1,'diagram interpretation','Marks altitude perpendicular to AB, not along a leg.')],
 ['A11.4','A11.8'], 'Using a leg as the hypotenuse; assuming a leg is the altitude to AB.', None)

item('Triangles','S','Matching triangles',
 'In triangles ABC and DEF, AB = DE = 6 cm, AC = DF = 8 cm, and ∠BAC = ∠EDF = 90°. Also BC = 10 cm.',
 [('a',6,'Explain whether these data guarantee congruence. State the vertex correspondence and find EF.'),('b',4,'A second claim says that any two triangles with corresponding side lengths 7 and 9 and a corresponding angle of 50° are congruent, even if that angle is not between the stated sides. Explain why this claim is not generally justified.')],
 [('a','SAS applies because the 90° angle is included between the matching 6 and 8 sides. A↔D, B↔E, C↔F, so EF = BC = 10 cm. The 6–8–10 side lengths are consistent with the right angle.'),('b','Removing the included-angle requirement can leave SSA data, which do not generally determine a unique triangle. In this separate claim, a side of length 7 opposite 50° and another side of length 9 can produce two triangles: a ray and a circle can meet in two possible third vertices. No numerical construction or sine law is required; a clear SSA ambiguity explanation or sketch suffices.')],
 [('a',2,'SAS','Names or describes included-angle congruence.'),('a',2,'correspondence','Gives A↔D, B↔E, C↔F.'),('a',2,'corresponding sides','Finds EF = 10 cm.'),('b',2,'necessary hypothesis','Identifies the missing included-angle condition.'),('b',2,'SSA ambiguity','Explains that an alternative third vertex can exist, or clearly states SSA is not a general congruence rule.')],
 ['A11.5','H12'], 'Using SSA as a general congruence rule; matching vertices by written order alone.', None)

item('Triangles','S','Similarity across a triangle',
 'D lies on AB and E lies on AC in triangle ABC, with DE parallel to BC. AD = 6 cm, DB = 3 cm, AE = 8 cm, and BC = 12 cm.',
 [('a',5,'Explain which triangles are similar and find EC.'),('b',5,'Find DE and the ratio of the area of triangle ADE to the area of triangle ABC. Explain why the two ratios differ.')],
 [('a','ADE and ABC are similar by shared angle A and corresponding angles from DE ∥ BC. AD/AB = 6/9 = 2/3, so AE/AC = 2/3. AC = 12 and EC = 4 cm.'),('b','DE = (2/3)(12) = 8 cm. The area ratio is (2/3)² = 4/9 because both a base and its corresponding altitude scale by 2/3.')],
 [('a',2,'AA similarity','Explains similarity and correspondence.'),('a',1,'whole-side ratio','Uses AB = 9 and ratio 2/3.'),('a',2,'side proportion','Finds AC = 12 and EC = 4.'),('b',2,'side proportion','Finds DE = 8 cm.'),('b',3,'area scaling','Finds 4/9 (1), explains two independent linear factors (2).')],
 ['A11.6','A15.1'], 'Using AD/DB as the scale factor; scaling areas linearly.', 'similar')

item('Triangles','S','Right-triangle trigonometry',
 'A 12 m cable runs from level ground to the top of a vertical pole, making an angle of 30° with the ground. In a separate setup, a 10 m cable makes an acute angle θ with level ground.',
 [('a',4,'For the 12 m cable, find the pole height and horizontal ground distance exactly. Explain your trig ratios or special-triangle relationships.'),('b',3,'For the separate 10 m cable, express the vertical height and horizontal distance in terms of θ. Explain which side is opposite and which is adjacent to θ.'),('c',3,'A separate square has side length 3 cm. Find its diagonal exactly and explain the right-triangle relationship you use.')],
 [('a','The cable is the hypotenuse. Height = 12 sin 30° = 6 m. Ground distance = 12 cos 30° = 6√3 m, using the 1:√3:2 ratio.'),('b','Height = 10 sin θ m; horizontal distance = 10 cos θ m. The vertical leg is opposite the angle at the ground; the horizontal leg is adjacent. Symbolic expressions are exact and need no calculator.'),('c','The diagonal divides the square into two 45°–45°–90° triangles. Its length is 3√2 cm. Equivalently d² = 3² + 3² = 18, so d = √18 = 3√2 cm.')],
 [('a',2,'30-60-90 lengths','Height 6 m and horizontal distance 6√3 m (1 each).'),('a',2,'right-triangle ratios','Uses the cable as hypotenuse with correct sine/cosine or special-triangle ratios.'),('b',2,'symbolic trig','10 sin θ and 10 cos θ (1 each).'),('b',1,'side identification','Explains opposite vertical and adjacent horizontal legs.'),('c',2,'45-45-90 structure','Uses d² = 3² + 3² or diagonal-to-side factor √2.'),('c',1,'exact diagonal','Obtains 3√2 cm.')],
 ['T','A11.7'], 'Swapping sine and cosine; treating the cable as a leg.', None)

item('Triangles','A','A hidden similarity in a right triangle',
 'Triangle ABC is right-angled at C. The perpendicular from C meets hypotenuse AB at D. AD = 4 cm and DB = 9 cm.',
 [('a',6,'Find CD exactly, explaining any similar triangles or other geometric relationships you use.'),('b',4,'Find AC and BC exactly. Show a method that checks your values against AB.')],
 [('a','Triangles ACD and CBD are similar: both have a right angle at D, and each other acute angle complements the same angle in ABC. Matching sides gives AD/CD = CD/DB, so CD² = 4·9 = 36 and CD = 6 cm. One may also set AC² = 16 + h² and BC² = 81 + h², then AC² + BC² = 169, giving h² = 36.'),('b','AB = 13 cm. AC² = AD² + CD² = 16 + 36 = 52, so AC = 2√13 cm. BC² = 81 + 36 = 117, so BC = 3√13 cm. Check: 52 + 117 = 169 = 13². Projection relations AC² = AB·AD and BC² = AB·DB are valid if justified.')],
 [('a',2,'hidden structure','Identifies valid similarity/correspondence or coupled Pythagorean equations.'),('a',2,'height relation','Derives h² = 36 with reasons.'),('a',2,'exact altitude','Gets CD = 6 cm.'),('b',1,'leg recovery','Finds AC = 2√13.'),('b',1,'leg recovery','Finds BC = 3√13.'),('b',2,'checking','Checks the squared lengths against AB² = 169.')],
 ['A11.6','Z8.3'], 'Assuming altitude bisects the hypotenuse; applying a projection formula to the wrong leg.', 'altitude')

item('Circles','F','Central and inscribed angles',
 'A and B lie on a circle with center O. The minor central angle AOB is 124°. C lies on the major arc AB and is distinct from A and B.',
 [('a',6,'Find the minor arc AB measure and ∠ACB. State the relationship between them.'),('b',4,'Point D instead lies on the minor arc AB, distinct from A and B. Find ∠ADB and explain which arc it intercepts.')],
 [('a','The minor arc measures 124°. C on the major arc sees the minor arc, so ∠ACB = 124°/2 = 62°.'),('b','D on the minor arc intercepts the major arc of 360° − 124° = 236°. Thus ∠ADB = 118°. Inscribed angles intercept the arc not containing their vertex.')],
 [('a',2,'central angle','Minor arc = 124°.'),('a',2,'inscribed angle','∠ACB = 62°.'),('a',2,'arc relationship','Explains central angle equals arc and inscribed angle is half intercepted arc.'),('b',2,'arc selection','Chooses major arc 236°.'),('b',2,'inscribed angle','Finds 118° with half-arc reasoning.')],
 ['A10.4','A10.5','Z8.2'], 'Always halving the minor arc regardless of vertex location.', 'circle_angles')

item('Circles','S','A tangent from an exterior point',
 'PT is tangent to a circle with center O at T. OT = 5 cm and OP = 13 cm. The line from P through O meets the circle first at A and then at B.',
 [('a',5,'Find PT exactly and explain the right angle you use.'),('b',5,'Find PA and PB. Verify that PT² and PA·PB agree, and distinguish the external secant segment from the whole secant.')],
 [('a','A radius to the tangent point is perpendicular to the tangent. PT² = 13² − 5² = 144, so PT = 12 cm.'),('b','PA = OP − r = 8 cm; PB = OP + r = 18 cm. PT² = 144 and PA·PB = 8·18 = 144. PA is external; PB is the entire secant from P to its farther intersection.')],
 [('a',2,'tangent perpendicularity','Identifies OT ⟂ PT.'),('a',3,'tangent length','Correct Pythagorean setup (1), PT = 12 cm (2).'),('b',2,'secant segments','PA = 8 and PB = 18 (1 each).'),('b',2,'power check','Computes and compares both products at 144.'),('b',1,'whole vs part','Correctly distinguishes PA from PB.')],
 ['A9','A17.1'], 'Subtracting the diameter instead of radius; multiplying external by only the internal portion.', 'tangent')

item('Circles','S','Intersecting chords',
 'Parts (a) and (b) describe separate circles. In (a), chords AB and CD intersect at X inside a circle, with AX = 3 cm, XB = 8 cm, and CX = 4 cm. In (b), chords EF and GH intersect at Y in another circle; the arc EG not containing F or H is 80°, and the arc FH not containing E or G is 120°.',
 [('a',5,'Find XD in the first circle, stating the segment relationship you use.'),('b',5,'Draw the second configuration and find ∠EYG, explaining which arcs determine it. Do not transfer the lengths from part (a) to this separate circle.')],
 [('a','Intersecting-chord products give AX·XB = CX·XD. Hence 3·8 = 4·XD and XD = 6 cm.'),('b','For chords crossing inside, ∠EYG = (arc EG + arc FH)/2 = (80° + 120°)/2 = 100°. These are the arcs intercepted by the angle and its vertical angle. The circles are separate, so the first part imposes no length restrictions on the second.')],
 [('a',3,'chord products','Uses the two parts of each same chord: 3·8 = 4·XD.'),('a',2,'segment calculation','Finds XD = 6 cm.'),('b',2,'arc identification','Sketches the second circle and selects EG and FH, not adjacent arcs.'),('b',3,'interior chord angle','Uses half the sum (2), gets 100° (1).')],
 ['A10.5','A17.1'], 'Using half a difference for an interior intersection; multiplying segments on different chords.', 'chords')

item('Circles','S','A cyclic quadrilateral',
 'A, B, C, and D occur in that order on one circle. In quadrilateral ABCD, ∠DAB = 3x + 10° and ∠BCD = 5x − 6°. Also ∠ABC = 110°. Side CD is extended through D to E.',
 [('a',6,'Find x and all four interior angles of ABCD.'),('b',4,'Find ∠ADE and explain why it equals one of the opposite interior angles.')],
 [('a','Opposite angles of a cyclic quadrilateral are supplementary: (3x + 10) + (5x − 6) = 180, so x = 22. A = 76°, C = 104°, B = 110°, and D = 70°.'),('b','∠ADE = 180° − 70° = 110°, equal to ∠ABC. The exterior angle is supplementary to D, and so is B; therefore they are equal.')],
 [('a',2,'cyclic relation','Sets opposite angles to sum to 180°.'),('a',1,'linear algebra','Finds x = 22.'),('a',3,'angle recovery','A and C correct (1 each); D = 70° with B = 110° retained (1).'),('b',2,'exterior angle','Finds 110°.'),('b',2,'justification','Connects the exterior supplement and the opposite interior supplement.')],
 ['A10.5','Z8.4'], 'Assuming adjacent cyclic angles are supplementary; extending the wrong side.', None)

item('Circles','A','A chord controls an arc',
 'A circle has radius 10 cm. Chord AB has length 12 cm. M is the midpoint of AB, and O is the center.',
 [('a',5,'Find OM and explain why triangle OMA is right-angled.'),('b',5,'Let φ = ∠AOM be acute. Express the minor central angle AOB and the length of the minor arc AB exactly using inverse trigonometry. State the angle units you use for arc length.')],
 [('a','OA = OB and AM = MB, so the center-to-midpoint line is perpendicular to the chord (by symmetry or congruent triangles). AM = 6; OM = √(100 − 36) = 8 cm.'),('b','sin φ = 6/10 = 3/5 (or tan φ = 3/4). The minor central angle is 2 arcsin(3/5) radians, and arc length is rθ = 20 arcsin(3/5) cm. Equivalent forms using arctan(3/4) or arccos(4/5) earn full credit. No decimal evaluation is required.')],
 [('a',2,'chord symmetry','Explains OM perpendicular to AB and AM = 6.'),('a',3,'distance','Sets up 10² − 6² (1) and gets 8 cm (2).'),('b',2,'inverse trig','Obtains φ from a correct ratio.'),('b',1,'central angle','Doubles φ for the minor central angle.'),('b',2,'arc length','Uses radians and rθ for 20 arcsin(3/5) cm (1 each).')],
 ['A9','A10.4','T'], 'Using the chord as arc length; forgetting to double the half-angle; substituting degrees directly into rθ.', 'chord_mid')

item('Area','F','A cut-out rectangle',
 'A rectangle is 12 cm wide and 9 cm high. A 4 cm by 3 cm rectangle is removed from its upper-right corner.',
 [('a',6,'Sketch the remaining L-shaped region and find its area.'),('b',4,'Find the perimeter of the remaining region. Explain why subtracting the cut-out perimeter from the original perimeter would be wrong.')],
 [('a','Original area = 12·9 = 108 cm². Remove 4·3 = 12 cm², leaving 96 cm².'),('b','The new boundary lengths are 12, 6, 4, 3, 8, and 9 cm, totaling 42 cm. Removing the corner replaces boundary lengths 4 and 3 by new lengths 4 and 3; the perimeter remains 2(12 + 9) = 42 cm.')],
 [('a',2,'region interpretation','Sketches a corner removal with consistent dimensions.'),('a',2,'area subtraction','Shows 108 − 12.'),('a',2,'area units','Gets 96 cm².'),('b',2,'boundary tracing','Finds perimeter 42 cm.'),('b',2,'boundary explanation','Explains the replaced boundary lengths; rejects subtracting all four cut-out edges.')],
 ['A15.3'], 'Mixing area and perimeter; counting interior edges as boundary.', None)

item('Area','S','Two diagonals and a height',
 'A rhombus has perpendicular diagonals of lengths 10 cm and 24 cm. A separate parallelogram has base 13 cm and perpendicular height 8 cm.',
 [('a',6,'Find the rhombus area by decomposing it into triangles. Find its side length as a check on your sketch.'),('b',4,'Find the parallelogram area. A learner uses a sloping side of length 10 cm as the height instead. Explain the error.')],
 [('a','The diagonals bisect each other. Four right triangles have legs 5 and 12 cm, each area 30 cm²; total area is 120 cm². The side is √(5² + 12²) = 13 cm.'),('b','Area = base times perpendicular height = 13·8 = 104 cm². A sloping side is not the perpendicular distance between parallel bases, so 13·10 is not justified.')],
 [('a',2,'decomposition','Uses half-diagonals 5 and 12 and four triangles.'),('a',2,'rhombus area','Finds 120 cm².'),('a',2,'length check','Finds the side 13 cm.'),('b',2,'perpendicular height','Finds 104 cm².'),('b',2,'error analysis','Explains why sloping length cannot replace perpendicular height.')],
 ['A12.4','A15.2','Z8.3'], 'Using full diagonals as triangle legs; confusing sloping and perpendicular height.', None)

item('Area','S','A circular segment',
 'In a circle of radius 6 cm, the minor central angle AOB is 120°. The minor circular segment is the region between chord AB and its minor arc.',
 [('a',4,'Find the area of minor sector AOB.'),('b',6,'Find the area of the minor circular segment exactly. Show how you find the triangle area without the laws of sines or cosines.')],
 [('a','Sector area = (120/360)π·6² = 12π cm².'),('b','Bisect the 120° angle and drop a perpendicular from O to AB. Each right triangle has hypotenuse 6 and central angle 60°, giving half-base 3√3 and height 3. Triangle AOB has area (1/2)(6√3)(3) = 9√3 cm². Segment area = 12π − 9√3 cm². Using (1/2)r² sin 120° is valid basic trig if the height relationship is explained.')],
 [('a',2,'sector fraction','Uses one third of the circle.'),('a',2,'sector area','Finds 12π cm².'),('b',2,'right-triangle construction','Draws/identifies the perpendicular that bisects the isosceles triangle.'),('b',2,'triangle area','Gets 9√3 from a correct base and height or justified trig height.'),('b',2,'region subtraction','Subtracts triangle from sector: 12π − 9√3 cm².')],
 ['A10.4','A11.7','A15.3','T'], 'Confusing sector with segment; subtracting the wrong triangle.', 'sector')

item('Area','A','Recover a triangle from its inner strip',
 'D lies on AB and E on AC in triangle ABC, with DE parallel to BC. AD:DB = 2:1. The area of quadrilateral DBCE is 45 cm².',
 [('a',6,'Find the areas of triangle ABC and triangle ADE. Explain how the given length ratio determines an area ratio.'),('b',4,'A second segment parallel to BC cuts off a triangle at A whose area is half the area of ABC. Find its side-length scale factor relative to ABC, and explain why that factor is not 1/2.')],
 [('a','AD/AB = 2/3, so [ADE]/[ABC] = 4/9. The strip DBCE is 5/9 of the whole. Therefore [ABC] = 45·9/5 = 81 cm² and [ADE] = 36 cm².'),('b','If the length factor is k, its area factor is k². Set k² = 1/2; positive k = 1/√2 = √2/2. A factor 1/2 in length would give 1/4 in area.')],
 [('a',2,'whole-side ratio','Uses linear ratio 2/3.'),('a',2,'complement area','Squares to 4/9 and uses strip fraction 5/9 (1 each).'),('a',2,'area recovery','81 and 36 cm² (1 each).'),('b',2,'inverse scaling','Sets k² = 1/2.'),('b',2,'exact factor','Finds √2/2 and explains why linear half is incorrect.')],
 ['A11.6','A15.1','Z8.3'], 'Using 2:1 directly as small-to-whole; treating the strip as half the whole.', 'similar')

item('Volume','F','A prism and a cylinder',
 'A right triangular prism has a right-triangle base with perpendicular legs 6 cm and 8 cm, and length 10 cm. A separate cylinder has radius 3 cm and height 5 cm.',
 [('a',5,'Find the prism volume, showing its base area.'),('b',5,'Find the cylinder volume. Explain the common geometric structure in the two volume calculations and state the units.')],
 [('a','Triangular base area = (1/2)(6)(8) = 24 cm². Volume = 24·10 = 240 cm³.'),('b','Circular base area = π·3² = 9π cm². Volume = 9π·5 = 45π cm³. Both use constant cross-sectional/base area times perpendicular length or height, producing cubic units.')],
 [('a',2,'base area','Finds triangular base area 24 cm².'),('a',3,'prism volume','Multiplies by prism length (1), finds 240 cm³ (2).'),('b',2,'cylinder formula','Uses πr²h.'),('b',2,'exact volume','Finds 45π cm³.'),('b',1,'dimensional meaning','Explains base area times height and cubic units.')],
 ['A18.1','A18.4'], 'Omitting the triangle factor 1/2; multiplying perimeter by height for volume.', None)

item('Volume','S','A tank with a conical roof',
 'A closed solid consists of a right circular cylinder of radius 3 cm and height 8 cm, topped by a right circular cone of the same radius and perpendicular height 4 cm. Their circular joining faces coincide, and their interiors do not overlap.',
 [('a',6,'Find the total solid volume. Label the two heights in a sketch.'),('b',4,'A geometrically similar solid has every length doubled. Find its volume and the ratio of new volume to original volume. Explain the scale factor.')],
 [('a','Cylinder: π·3²·8 = 72π. Cone: (1/3)π·3²·4 = 12π. Total = 84π cm³. The cone height is its perpendicular 4 cm height, not the sloping edge.'),('b','Doubling three linear dimensions multiplies volume by 2³ = 8, so new volume = 672π cm³. New:original volume = 8:1.')],
 [('a',2,'solid interpretation','Sketch distinguishes cylinder height 8 and cone height 4.'),('a',2,'component volumes','72π cylinder and 12π cone (1 each).'),('a',2,'volume addition','Adds to 84π cm³.'),('b',2,'volume scaling','Uses factor 8 and explains cubic scaling.'),('b',2,'scaled volume','672π cm³ and ratio 8:1.')],
 ['A18.4','A18.5'], 'Using total height for each component; forgetting cone factor 1/3; doubling volume instead of cubing scale.', 'roof')

item('Volume','S','Material left after drilling',
 'In (a), a cube has side length 10 cm. A cylindrical hole of radius 2 cm is drilled straight through its center, perpendicular to two opposite faces. No material outside the cylinder is removed. Part (b) concerns a separate hollow sphere.',
 [('a',6,'Find the volume of material remaining in the cube. Draw or describe the removed cylinder dimensions.'),('b',4,'A hollow sphere has outer radius 5 cm and concentric inner radius 3 cm. Find its material volume exactly. Explain why inserting the wall thickness as the radius of a solid sphere would be incorrect.')],
 [('a','Cube volume = 1000 cm³. The hole is a radius-2, height-10 cylinder, of volume 40π cm³. Remaining volume is 1000 − 40π cm³.'),('b','Material volume = (4/3)π(5³ − 3³) = (4/3)π(98) = 392π/3 cm³. A solid sphere of radius 5 − 3 = 2 cm is a different region. Cubing the difference is not the same as subtracting the cubes.')],
 [('a',2,'hole dimensions','Uses radius 2 and cylinder length 10.'),('a',2,'removed volume','Computes 40π cm³.'),('a',2,'subtraction','Finds 1000 − 40π cm³.'),('b',2,'spherical shell','Subtracts full sphere volumes with the correct 4π/3 factor.'),('b',1,'exact volume','Gets 392π/3 cm³.'),('b',1,'region interpretation','Explains why a radius-2 solid sphere is not the shell.')],
 ['A18.2','A18.3','A18.4'], 'Using diameter as radius; subtracting only an opening area; cubing wall thickness instead of subtracting two sphere volumes.', None)

item('Surface area','F','An open rectangular box',
 'A thin-walled rectangular box has internal and external dimensions treated as identical: length 8 cm, width 5 cm, height 3 cm. It has a bottom and four side walls, but no lid. Ignore wall thickness and count only one side of each material panel.',
 [('a',6,'Sketch a possible net, label its panels, and find the total panel area.'),('b',4,'Find the extra area needed to add a lid. Explain how the no-lid instruction changes the closed-box surface-area calculation.')],
 [('a','The net has one 8×5 bottom, two 8×3 walls, and two 5×3 walls. Area = 40 + 48 + 30 = 118 cm².'),('b','A lid adds 8·5 = 40 cm². Closed-box area is 158 cm², so the open-box area is 158 − 40 = 118 cm². Counting both physical sides would be a different question.')],
 [('a',2,'net','Shows one bottom and four suitably joined side panels.'),('a',2,'panel dimensions','Labels 8×5, two 8×3, and two 5×3 panels.'),('a',2,'area sum','Finds 118 cm².'),('b',2,'missing face','Finds lid area 40 cm².'),('b',2,'open vs closed','Explains omission of exactly one base; closed total 158 cm².')],
 ['A18.1','A18.3','G10.4'], 'Including a lid; counting a face twice; reporting cubic units.', None)

item('Surface area','S','Cylinder net and missing end',
 'A cylinder has radius 3 cm and height 10 cm. First consider the closed cylinder, then the same cylinder with its upper circular face removed. Ignore thickness and count each surface once.',
 [('a',5,'Sketch the net of the closed cylinder. Label the rectangle dimensions and find both its lateral area and total surface area.'),('b',2,'Find the surface area after the upper face is removed. Explain precisely which area disappears.'),('c',3,'A separate sphere has radius 3 cm. Find its surface area and explain why using the area of one circular disk would not answer this question.')],
 [('a','The curved surface unwraps into a rectangle of width 2πr = 6π cm and height 10 cm. Lateral area = 60π cm². The two disks add 18π, giving total surface area 78π cm².'),('b','One disk has area 9π cm². Removing the upper face leaves 60π + 9π = 69π cm². The bottom disk and the full curved wall remain.'),('c','Sphere surface area = 4πr² = 36π cm². A disk area πr² = 9π describes a flat cross-section, not the entire curved spherical surface.')],
 [('a',2,'cylinder net','Labels rectangle 6π by 10 and includes two radius-3 disks.'),('a',1,'lateral area','Finds 60π cm².'),('a',2,'total area','Adds two disks for 78π cm².'),('b',1,'face removal','Subtracts one disk of 9π.'),('b',1,'open surface','Gets 69π cm² and describes remaining surfaces.'),('c',2,'sphere area','Uses 4πr² (1), obtains 36π cm² (1).'),('c',1,'cross-section vs surface','Distinguishes one flat disk from the whole sphere surface.')],
 ['A18.2','A18.4','G10.4'], 'Unwrapping to diameter by height; confusing lateral area and total area; confusing a sphere with a disk.', None)

item('Surface area','A','Exposed surfaces of a joined solid',
 'A closed solid consists of a cylinder of radius 3 cm and height 8 cm, topped by a cone of the same radius and perpendicular height 4 cm. Their circular joining faces coincide. Only the exterior surface is to be painted; include the bottom disk.',
 [('a',6,'Find the cone slant height and the total exterior area to be painted. Explain which surfaces are hidden.'),('b',4,'A model has all lengths multiplied by 3. Find its exterior area. Explain why simply adding the full surface areas of the original cone and cylinder would overcount.')],
 [('a','Cone slant height is √(3² + 4²) = 5 cm. Exposed areas: cylinder wall 2π·3·8 = 48π; cone wall π·3·5 = 15π; bottom disk 9π. Total = 72π cm². Both coincident joining disks are internal and excluded.'),('b','Area scales by 3² = 9, so model exterior area = 648π cm². Full cone plus full cylinder areas count the common circular interface twice, overcounting by 2πr² = 18π cm² for the original solid.')],
 [('a',2,'slant vs height','Uses right triangle to get slant height 5.'),('a',2,'curved areas','Finds 48π cylinder wall and 15π cone wall (1 each).'),('a',2,'exposed area','Includes only bottom disk and totals 72π.'),('b',2,'area scaling','Uses factor 9 and obtains 648π cm².'),('b',2,'internal interface','Explains two hidden disks and overcount 18π cm².')],
 ['A18.4','A18.5','G10.4'], 'Using perpendicular cone height in lateral area; counting the hidden joining disks; cubing the area scale.', 'roof')

REFERENCES = {
 'A10.1': 'AoPS Vol. 1, §10.1, Lines, Rays, and Segments, p. 84.',
 'A10.2': 'AoPS Vol. 1, §10.2, Classification and Measurement, pp. 84–86.',
 'A10.3': 'AoPS Vol. 1, §10.3, Angles and Parallel Lines, p. 86.',
 'A10.4': 'AoPS Vol. 1, §10.4, Arcs, Segments, Sectors, and Angles, p. 87.',
 'A10.5': 'AoPS Vol. 1, §10.5, Angles Formed By Lines Intersecting a Circle, pp. 87–90.',
 'A11.1': 'AoPS Vol. 1, §11.1, Classifying Triangles, p. 93.',
 'A11.3': 'AoPS Vol. 1, §11.3, The Triangle Inequality, p. 96.',
 'A11.4': 'AoPS Vol. 1, §11.4, The Pythagorean Theorem, pp. 97–99.',
 'A11.5': 'AoPS Vol. 1, §11.5, Congruent Triangles, pp. 99–102.',
 'A11.6': 'AoPS Vol. 1, §11.6, Similar Triangles, pp. 102–104.',
 'A11.7': 'AoPS Vol. 1, §11.7, Introduction to Trigonometry, pp. 104–109.',
 'A11.8': 'AoPS Vol. 1, §11.8, Area of a Triangle, p. 109.',
 'A12.3': 'AoPS Vol. 1, §12.3, Parallelograms, p. 120.',
 'A12.4': 'AoPS Vol. 1, §12.4, Rhombuses (Rhombi?), p. 121.',
 'A13.2': 'AoPS Vol. 1, §13.2, Angles in a Polygon, p. 128.',
 'A13.3': 'AoPS Vol. 1, §13.3, Regular Polygons, p. 128.',
 'A14': 'AoPS Vol. 1, Chapter 14, Angle Chasing, pp. 133–135.',
 'A15.1': 'AoPS Vol. 1, §15.1, Similar Figures, p. 136.',
 'A15.2': 'AoPS Vol. 1, §15.2, Same Base/Same Altitude, p. 137.',
 'A15.3': 'AoPS Vol. 1, §15.3, Complicated Figures, pp. 138–142.',
 'A16': 'AoPS Vol. 1, Chapter 16, The Power of Coordinates, pp. 143–154; especially §§16.3–16.6.',
 'A17.1': 'AoPS Vol. 1, §17.1, Introduction [Power of a Point], p. 155.',
 'A18.1': 'AoPS Vol. 1, §18.1, Planes, Surface Area, and Volume, p. 160.',
 'A18.2': 'AoPS Vol. 1, §18.2, Spheres, p. 161.',
 'A18.3': 'AoPS Vol. 1, §18.3, Cubes and Boxes, pp. 162–165.',
 'A18.4': 'AoPS Vol. 1, §18.4, Prisms and Cylinders, p. 165.',
 'A18.5': 'AoPS Vol. 1, §18.5, Pyramids and Cones, pp. 166–168.',
 'A9': 'AoPS Vol. 1, Chapter 9, An Introduction to Circles, pp. 81–83.',
 'Z8.2': 'Zeitz, 2nd ed., §8.2, Survival Geometry I, pp. 258–269; lines/triangles pp. 259–263; circles pp. 264–269.',
 'Z8.3': 'Zeitz, 2nd ed., §8.3, Survival Geometry II: Area (p. 270), Similar Triangles (p. 274).',
 'Z8.4': 'Zeitz, 2nd ed., §8.4, The Power of Elementary Geometry: Concyclic Points, p. 283.',
 'H12': 'Houston, local manuscript, Chapter 12, Examples and counterexamples, p. 92.',
 'T': 'AoPS Vol. 1, §11.7, Introduction to Trigonometry, pp. 104–109; vault Trigonometry, Section 2.2 - Radian Measure (Converting section only); geometry-trigonometry-interpretation-practice, questions 3, 8, 10, 15.',
 'G10.4': 'Akiyama & Matsunaga, Treks into Intuitive Geometry, 2nd ed. (2024), Chapter 10 §4, Eleven Types of e-Nets of a Cube, pp. 407–413. Enrichment for unfolding and surface interpretation; not a prerequisite for the elementary box/cylinder net tasks.'
}

STYLE = ParagraphStyle('text', fontName='Body', fontSize=10.5, leading=15, textColor=INK)
SMALL = ParagraphStyle('small', parent=STYLE, fontSize=9, leading=12.5)
HEAD = ParagraphStyle('head', parent=STYLE, fontName='Bold', fontSize=18, leading=23)

def normalized(text):
 return str(text).replace('–','-').replace('—','-').replace('‑','-')

def markup(text):
 text=normalized(text)
 for ch in '∠∥⟂':text=text.replace(ch,f'<font name="Math">{ch}</font>')
 return text

class Doc:
 def __init__(self,path,kind):
  self.c=canvas.Canvas(str(path),pagesize=(W,H));self.kind=kind;self.page=0;self.y=0
  self.c.setTitle('Geometry Mastery Diagnostic' if kind=='Student assessment' else 'Geometry Mastery Diagnostic - Solutions, Grading Rubric, and Skill Profile')
  self.c.setAuthor('Lexicon of the Arcane');self.path=path
 def new(self,section):
  if self.page:self.footer();self.c.showPage()
  self.page+=1;self.c.setFillColor(ACCENT);self.c.rect(42,H-46,528,3,fill=1,stroke=0)
  self.c.setFont('Bold',9);self.c.drawString(42,H-33,'GEOMETRY MASTERY DIAGNOSTIC')
  self.c.setFont('Body',8);self.c.drawRightString(570,H-33,self.kind)
  self.y=H-72;self.p(section,HEAD);self.gap(10)
 def p(self,text,style=STYLE):
  p=Paragraph(markup(text),style);_,h=p.wrap(528,700)
  if self.y-h<48:raise RuntimeError(f'Overflow {self.kind} page {self.page}: {text[:60]}')
  p.drawOn(self.c,42,self.y-h);self.y-=h+7
 def gap(self,n):self.y-=n
 def rule(self):
  self.c.setStrokeColor(LIGHT);self.c.line(42,self.y,570,self.y);self.y-=12
 def footer(self):
  self.c.setFillColor(GRAY);self.c.setFont('Body',8)
  self.c.drawString(42,29,'Version 1.0 • 28 October 2026 • '+self.kind)
  self.c.drawRightString(570,29,str(self.page))
 def save(self):self.footer();self.c.save()
 def table(self,rows,widths,fontsize=9):
  x0=42
  sty=ParagraphStyle('cell',parent=SMALL,fontSize=fontsize,leading=fontsize+3)
  for ri,row in enumerate(rows):
   cells=[];ht=0
   for text,w in zip(row,widths):
    p=Paragraph(markup(text),sty);_,h=p.wrap(w-12,600);cells.append((p,h));ht=max(ht,h+12)
   if self.y-ht<48:raise RuntimeError('Table overflow')
   x=x0
   for (p,h),w in zip(cells,widths):
    self.c.setFillColor(colors.HexColor('#edf2f4') if ri==0 else colors.white)
    self.c.setStrokeColor(LIGHT);self.c.rect(x,self.y-ht,w,ht,fill=1,stroke=1)
    p.drawOn(self.c,x+6,self.y-6-h);x+=w
   self.y-=ht
  self.y-=10

def draw_diagram(doc,kind):
 if not kind:return
 c=doc.c; top=doc.y; bottom=top-125
 c.saveState();c.translate(130,bottom+10);c.setStrokeColor(INK);c.setFillColor(INK);c.setLineWidth(1.2)
 def L(x,y,s,dx=0,dy=0):
  tx=x+dx
  for ch in normalized(s):
   font='Math' if ch in '∠∥⟂' else 'Body'
   c.setFont(font,10);c.drawString(tx,y+dy,ch);tx+=pdfmetrics.stringWidth(ch,font,10)
 def line(a,b):c.line(*a,*b)
 def poly(points,close=False):
  p=c.beginPath();p.moveTo(*points[0])
  for pt in points[1:]:p.lineTo(*pt)
  if close:p.close()
  c.drawPath(p)
 def point(a,name,dx=5,dy=5):c.circle(*a,1.8,fill=1);L(*a,name,dx,dy)
 if kind=='segments':
  line((0,55),(330,55))
  for x,n in [(10,'A'),(160,'M'),(310,'B')]:point((x,55),n,-3,10)
  L(45,30,'3x − 2 cm');L(205,30,'x + 6 cm')
 elif kind=='parallel':
  line((0,82),(300,82));line((0,22),(300,22));line((85,0),(200,110))
  L(310,80,'ℓ');L(310,20,'m');L(160,90,'P');L(112,5,'Q')
  L(190,87,'64°');L(130,29,'α');L(68,28,'β')
 elif kind in ['isosceles','hidden','similar','altitude','bisectors']:
  if kind=='isosceles':
   A=(140,105);B=(106.6,8);C=(173.4,8);poly([A,B,C,A]);line(C,(290,8))
   for p,n in [(A,'A'),(B,'B'),(C,'C'),((290,8),'D')]:point(p,n,3,-12 if n!='A' else 5)
   L(132,78,'38°');L(20,80,'AB = AC')
  elif kind=='hidden':
   A=(145,105);B=(112.5,5);C=(177.5,5);D=(165.08,43.21)
   poly([A,B,C,A]);line(B,D)
   for p,n in [(A,'A'),(B,'B'),(C,'C'),(D,'D')]:point(p,n,4,4)
   L(137,80,'36°');L(245,75,'AB = AC');L(245,57,'BD = BC')
  elif kind=='similar':
   A=(120,110);B=(0,5);C=(310,5);D=(40,40);E=(247,40)
   poly([A,B,C,A]);line(D,E)
   for p,n in [(A,'A'),(B,'B'),(C,'C'),(D,'D'),(E,'E')]:point(p,n,4,5)
   L(265,75,'DE ∥ BC')
  elif kind=='altitude':
   A=(0,5);B=(195,5);C=(60,95);D=(60,5)
   poly([A,B,C,A]);line(C,D);poly([(60,16),(71,16),(71,5)])
   for p,n in [(A,'A'),(B,'B'),(C,'C'),(D,'D')]:point(p,n,3,-12 if n!='C' else 5)
   L(25,16,'4');L(122,16,'9');L(215,85,'∠ACB = 90°')
  else:
   A=(0,5);B=(170,5);C=(209.3,102.4);D=(39.3,102.4);P=(117.0,83.9)
   poly([A,B,C,D,A]);line(A,P);line(B,P)
   for p,n in [(A,'A'),(B,'B'),(C,'C'),(D,'D'),(P,'P')]:point(p,n,4,4)
   L(270,70,'AP and BP:');L(270,54,'internal bisectors')
 elif kind in ['circle_angles','chords','chord_mid','sector','tangent']:
  O=(165,55) if kind=='chords' else (145,55);r=44 if kind=='chords' else 48;c.circle(*O,r)
  if kind=='circle_angles':
   A=(102.62,32.47);B=(187.38,32.47);C=(145,103)
   line(O,A);line(O,B);poly([A,C,B])
   for p,n in [(O,'O'),(A,'A'),(B,'B'),(C,'C')]:point(p,n,4,4)
   L(220,70,'∠AOB = 124°');L(220,50,'C on major arc AB')
  elif kind=='chords':
   A=(121,55);B=(209,55);C=(132.2,25.67);D=(164.2,98.99);X=(145,55)
   line(A,B);line(C,D)
   for p,n in [(A,'A'),(B,'B'),(C,'C'),(D,'D'),(X,'X')]:point(p,n,4,4)
   L(220,70,'Part (a) only');L(220,50,'AX = 3, XB = 8');L(220,30,'CX = 4')
  elif kind=='chord_mid':
   A=(183,26);B=(183,84);M=(183,55)
   line(A,B);line(O,A);line(O,B);line(O,M)
   for p,n in [(O,'O'),(A,'A'),(B,'B'),(M,'M')]:point(p,n,5,3)
   L(220,70,'r = 10 cm');L(220,50,'AB = 12 cm')
  elif kind=='sector':
   A=(103,31);B=(187,31);line(O,A);line(O,B);line(A,B)
   for p,n in [(O,'O'),(A,'A'),(B,'B')]:point(p,n,4,4)
   L(220,70,'r = 6 cm');L(220,50,'minor ∠AOB = 120°')
  else:
   P=(269.8,55);T=(163.4615,99.3077);A=(193,55);B=(97,55)
   line(P,T);line(O,T);line(B,P)
   for p,n in [(O,'O'),(P,'P'),(T,'T'),(A,'A'),(B,'B')]:point(p,n,4,4)
   L(35,100,'OT = 5');L(230,30,'OP = 13')
 elif kind=='roof':
  c.ellipse(75,0,185,18);c.ellipse(75,65,185,83)
  line((75,9),(75,74));line((185,9),(185,74));line((75,74),(130,112));line((185,74),(130,112))
  c.setDash(3,3);line((130,74),(130,112));line((130,9),(130,74));line((130,74),(185,74));c.setDash()
  L(195,37,'cylinder height 8');L(195,93,'cone height 4');L(190,70,'radius 3')
 c.restoreState();doc.y=bottom-8

def validate_data():
 assert len(QUESTIONS)==30
 assert collections.Counter(q['level'] for q in QUESTIONS)=={'F':10,'S':14,'A':6}
 expected={'Lines':4,'Angle chasing':5,'Triangles':6,'Circles':5,'Area':4,'Volume':3,'Surface area':3}
 assert collections.Counter(q['topic'] for q in QUESTIONS)==expected
 for q in QUESTIONS:
  assert sum(p[1] for p in q['parts'])==10
  assert sum(r[1] for r in q['rubric'])==10
  assert {p[0] for p in q['parts']}=={s[0] for s in q['solution']}
  for a,pts,_ in q['parts']:assert sum(r[1] for r in q['rubric'] if r[0]==a)==pts
  assert all(r in REFERENCES for r in q['refs'])
  assert all(term not in q['stem'].lower() for term in ['differentiate','integrate','law of cosines','law of sines'])

def student_pdf():
 d=Doc(OUT/'Geometry Mastery Diagnostic.pdf','Student assessment')
 d.new('Geometry Mastery Diagnostic')
 d.p('30 free-response questions • 300 points • Suggested time: 3–4 hours')
 d.gap(12);d.p('Name: ___________________________________   Date: ______________')
 d.p('Sitting 1: start ______ end ______   Sitting 2: start ______ end ______')
 d.gap(10);d.p('<b>Working conditions</b>')
 for s in [
  'Work independently, without a calculator, formula sheet, books, internet, or help. A ruler may be used to draw straight lines, but do not measure diagrams to obtain answers.',
  'Give exact answers: use fractions, radicals, π, or unevaluated trig/inverse-trig expressions as appropriate. State angle units, and include length, square, or cubic units when given.',
  'Show your setup and explain the geometric choices in your own words. A short clear explanation is enough; formal two-column proofs are not required. Unsupported correct answers earn only result points.',
  'Diagrams are schematic and are not necessarily to scale. Use only stated givens, marked relationships, and valid deductions. Add labels or draw your own sketch where useful.',
  'Attempt every question. If stuck, record what you can establish and move on. You may continue a later part using your earlier result; label that assumption. Each question is worth 10 points.',
  'If using two sittings, stop after Question 15. Do not study, consult solutions, or receive feedback between sittings. Record the break and total working time. Results from different conditions should be labeled accordingly.'
 ]:d.p('• '+s)
 d.gap(8);d.p('<b>Record your status after each question</b>')
 d.p('Write A = attempted, S = saw but skipped, or N = not reached. Confidence: 0 = guessing, 1 = uncertain, 2 = fairly sure, 3 = very sure. Confidence and time are not graded.')
 d.p('This is a diagnostic, so gaps are useful information. Do not consult the separate grader packet until you finish.')
 d.new('Assessment map and response guide')
 d.table([['Questions','Primary topic','Points'],['1–4','Lines','40'],['5–9','Angle chasing','50'],['10–15','Triangles','60'],['16–20','Circles','50'],['21–24','Area','40'],['25–27','Volume','30'],['28–30','Surface area','30']],[90,348,90])
 d.p('Some questions combine topics. Their points belong to the primary topic shown above; your grader may record secondary observations without adding those points twice.')
 d.gap(14);d.p('<b>Useful response habits</b>')
 d.p('Label each answer (a), (b), and so on. Make your equations readable, identify the quantities you calculate, and leave enough reasoning for someone else to follow your approach. Cross out discarded work rather than erasing every trace of your thinking.')
 d.p('Use the rest of each question page for calculations and diagrams. If you need more paper, label it with your name and question number and attach it to this packet.')
 d.gap(15);d.p('<b>Conditions and background - not graded</b>')
 for t in ['Most recent geometry course or self-study: ___________________________',
 'Prior familiarity with AoPS or contest geometry: ________________________',
 'Any accommodations or changes to the working conditions: ______________',
 '________________________________________________________________',
 'Approximate time since last regular geometry practice: _________________']:d.p(t)
 for q in QUESTIONS:
  d.new(f"{q['n']:02d}  {q['title']}")
  d.p(f"<b>{q['topic']} • 10 points</b>",SMALL)
  d.p(q['stem']);draw_diagram(d,q['diagram'])
  for label,pts,prompt in q['parts']:d.p(f'<b>({label}) [{pts} points]</b> {prompt}')
  d.rule();d.p('Work and explanation:',SMALL)
  c=d.c;c.setStrokeColor(LIGHT);c.setLineWidth(.35)
  yy=d.y-22
  while yy>100:c.line(42,yy,570,yy);yy-=27
  c.setFillColor(GRAY);c.setFont('Body',9)
  c.drawString(42,68,'Status (A / S / N): ______    Confidence (0–3): ______    Time: ______ min')
 d.save()

def grader_pdf():
 d=Doc(OUT/'Geometry Mastery Diagnostic - Solutions, Grading Rubric, and Skill Profile.pdf','Grader packet')
 d.new('Solutions, rubric, and skill profile')
 d.p('Companion to the 30-question assessment • 300 points • Keep separate from the student packet')
 d.gap(14);d.p('<b>Purpose and interpretation</b>')
 d.p('Identify what the learner understands, what breaks down, and what to practice next. The total score is secondary to the seven topic profiles and specific error patterns. These are provisional instructional judgments, not standardized, normed, or validated mastery cutoffs.')
 d.p('Question labels F / S / A mean foundational / standard / advanced. Difficulty is an author judgment, not an empirical item calibration. All items are original diagnostic questions aligned to the source sections listed later; none is reproduced or represented as a numbered textbook problem.')
 d.p('Source permission was reported by the requester. Original items were selected to control coverage and exact-answer arithmetic. Source alignments document concepts and remediation, rather than claiming derivation from a particular exercise.')
 d.gap(10);d.p('<b>Scoring policy</b>')
 for s in [
  'Use each question’s analytic rubric. Award only the stated points; each item totals 10. A response may earn reasoning credit even with an incorrect final answer. Any correct method within the test scope earns equivalent credit.',
  'Within a multi-point criterion, award the explicitly listed increments. If no increments are listed, award 0 for absent/incorrect work, full credit for the stated evidence, and intermediate whole points for correct but incomplete evidence.',
  'An unsupported correct result earns only the points explicitly assigned to that result, never points for a missing setup, explanation, or check. A correct labeled diagram can provide reasoning evidence where the rubric allows it.',
  'Penalize a local arithmetic/algebra error at its first affected criterion. Award later method and result points for correct follow-through on that value when it remains mathematically meaningful; mark FT. Do not penalize the same error again.',
  'If an early error makes a later task impossible or trivial, award any independently demonstrated method points; mark the unobserved skill for follow-up. Do not infer mastery of a skill the altered problem no longer tests.',
  'For dimensional quantities, a missing/wrong unit costs at most 1 point per question, within result points and never below zero. Accept unsimplified exact equivalents unless simplification itself is assessed.'
 ]:d.p('• '+s,SMALL)
 d.new('How to build a useful diagnosis')
 d.p('<b>1. Record evidence, not just a total</b>')
 d.p('Enter each question score, status, confidence, and the criterion-level skill missed. A = attempted, S = seen/skipped, N = not reached. Blank work earns 0 for score computation, but N is a coverage limitation, not evidence that the learner lacks the concept.')
 d.table([['Code','Error class','Use when the work shows…'],['C','Conceptual knowledge','A wrong relationship or misunderstood definition.'],['D','Diagram interpretation','Wrong vertex, region, angle sector, face, or point order.'],['S','Strategy selection','Relevant facts known, but no productive connection or setup.'],['J','Justification','An unsupported claim, omitted reason, or invalid generalization.'],['A','Algebra/arithmetic','A sound geometric setup followed by calculation error.'],['U','Units/formula recall','Missing formula, mismatched units, or wrong recalled formula.']],[48,144,336])
 d.p('Codes may overlap. Record U for an apparently forgotten formula; record C as well when the learner’s explanation shows a conceptual misconception. If the written work cannot distinguish recall from understanding, write “needs follow-up” rather than guessing.')
 d.p('<b>2. Compute the seven topic percentages</b>')
 d.p('Add primary-topic points only. Percentage = topic points earned ÷ topic maximum × 100. Do not average topic percentages to obtain the overall score; overall percentage is total points ÷ 300 × 100.')
 d.p('<b>3. Apply bands and the foundational gate</b>')
 d.table([['Topic percentage','Provisional interpretation'],['Below 50%','Rebuild foundations'],['50% to below 70%','Developing'],['70% to below 85%','Mostly secure'],['85%–100%','Strong evidence of mastery, only if foundational score ≥80%']],[140,388])
 d.p('If the topic percentage is at least 85% but its foundational score is below 80%, cap the label at “mostly secure - foundational gap.” If any item in that topic is not reached, show the raw score but mark the classification “incomplete”; administer the missed item without feedback before finalizing the topic label.',SMALL)
 d.new('Coverage, difficulty, and scoring map')
 rows=[['Topic','Questions / maximum','Foundational items / gate']]
 for topic in dict.fromkeys(q['topic'] for q in QUESTIONS):
  qs=[q for q in QUESTIONS if q['topic']==topic];fs=[q for q in qs if q['level']=='F']
  rows.append([topic,', '.join(str(q['n']) for q in qs)+f" / {10*len(qs)}",', '.join(str(q['n']) for q in fs)+f" / need {8*len(fs)} of {10*len(fs)}"])
 d.table(rows,[105,235,188],8.5)
 for level,name in [('F','Foundational'),('S','Standard'),('A','Advanced')]:
  ns=[str(q['n']) for q in QUESTIONS if q['level']==level]
  d.p(f'<b>{name}:</b> '+', '.join(ns)+f' ({len(ns)*10} points).')
 d.p('<b>Report advanced transfer separately</b>')
 d.p('Advanced transfer = points on Q4, Q9, Q15, Q20, Q24, Q30 out of 60. Record each item as well as the subtotal. Do not apply the topic mastery bands to this six-item sample: describe demonstrated successes and barriers. Advanced points remain in their primary-topic totals and in the overall 300; this separate report adds no points.')
 d.p('<b>Examples of interpreting patterns</b>')
 d.p('A high correct-answer rate with missing reasons suggests J, not automatically strong reasoning. A low score concentrated in A with correct geometric setups calls for calculation practice. A strong routine score but weak advanced transfer calls for unfamiliar configurations and strategy practice. High confidence on incorrect C/D responses is a priority misconception check.')
 for q in QUESTIONS:
  d.new(f"{q['n']:02d}  {q['title']}")
  d.p(f"<b>Primary topic: {q['topic']} • Level {q['level']} • 10 points • Original item</b>",SMALL)
  d.p('<b>Worked solution</b>')
  for part,text in q['solution']:d.p(f'<b>({part})</b> '+text)
  d.gap(3);d.p('<b>Analytic rubric</b>')
  rows=[['Part','Pts','Subskill','Observable evidence']]
  for part,pts,skill,evidence in q['rubric']:rows.append([part,str(pts),skill,evidence])
  d.table(rows,[35,30,125,338],8.5)
  d.p('<b>Diagnosis:</b> '+q['errors'],SMALL)
  d.p('<b>Review:</b> '+' '.join(REFERENCES[r] for r in q['refs']),SMALL)
  d.p('All criterion points on this page belong to the primary topic above. Secondary observations are descriptive only. Apply the general equivalent-method and follow-through policy.',SMALL)
 d.new('Score record - Questions 1–15')
 score_sheet(d,QUESTIONS[:15])
 d.new('Score record - Questions 16–30')
 score_sheet(d,QUESTIONS[15:])
 d.new('Topic profile and coverage')
 d.p('Learner: ______________________________   Grader/date: __________________')
 d.table([['Topic','Score / max','Foundation','N items','Band / main subskill gap']]+[
  [topic,f'____ / {10*sum(q["topic"]==topic for q in QUESTIONS)}','____ / '+str(10*sum(q['topic']==topic and q['level']=='F' for q in QUESTIONS)),'____','____________________']
  for topic in dict.fromkeys(q['topic'] for q in QUESTIONS)], [95,83,90,55,205],8)
 d.p('Overall: ______ / 300 = ______%    Foundational: ______ / 100')
 d.p('Standard: ______ / 140    Advanced transfer: ______ / 60')
 d.table([['Advanced item','Q4','Q9','Q15','Q20','Q24','Q30'],['Score / 10','____','____','____','____','____','____'],['Main obstacle','____','____','____','____','____','____']],[108,70,70,70,70,70,70],8)
 d.p('Advanced successes demonstrated: ______________________________________')
 d.p('___________________________________________________________________')
 d.p('Coverage flags and follow-up needed: ____________________________________')
 d.p('___________________________________________________________________')
 d.p('Use the band thresholds and foundational gates on the earlier pages. With only 3–6 questions per topic, inspect subskills before labeling the whole domain. High performance on one subskill does not establish mastery of every untested theorem.',SMALL)
 d.new('Study priorities and reassessment')
 d.p('<b>Choose the next steps</b>')
 d.p('First resolve incomplete coverage. Then prioritize repeated foundational C/D errors, followed by repeated strategy gaps, formula recall, and calculation errors. Use the topic band as a signal, not an automatic ranking. Within a topic, target the exact missed rubric subskills.')
 for i in range(1,4):
  d.p(f'<b>Priority {i}</b>')
  for line in ['Topic / subskill and evidence (question, criterion, error code): ______________',
    '________________________________________________________________',
    'Verified reading section and practice task: _____________________________',
    '________________________________________________________________',
    'Success check and reassessment date: __________________________________']:
   d.p(line,SMALL)
  d.gap(5)
 d.p('<b>Reassessment rule</b>')
 d.p('After targeted practice, use fresh questions with different numbers/configurations: at least two foundational and two application items per weak subskill where feasible. Require reasons as well as answers. Check retention after several days. Reusing this exact test measures familiarity as well as improvement; label any repeat administration.',SMALL)
 d.new('Remediation routes')
 routes=[
 ('Lines / angles','Q1–9','A10.1','A10.3','A14'),
 ('Triangle structure','Q10–12','A11.3','A11.4','A11.5'),
 ('Similarity / scaling','Q13, Q15, Q24','A11.6','A15.1','Z8.3'),
 ('Basic trig / arc units','Q14, Q20, Q23','A11.7','A10.4','T'),
 ('Circle relationships','Q16–20','A10.5','A17.1','Z8.2'),
 ('Area / decomposition','Q21–24','A15.2','A15.3','Z8.3'),
 ('Volume / exposed surfaces','Q25–30','A18.2','A18.3','A18.4','A18.5')]
 for name,qs,*refs in routes:
  d.p(f'<b>{name} ({qs})</b>',SMALL);d.p(' '.join(REFERENCES[r] for r in refs),SMALL)
 d.p('<b>Practice matched to the error</b>',SMALL)
 d.p('C: explain the definition and give an example/non-example. D: redraw and label the same structure in a new orientation. S: compare two plausible approaches and choose one. J: write the missing reason at each step. A: redo calculation from a correct setup and check independently. U: reconstruct the formula from a diagram or net before retrieval practice.',SMALL)
 d.new('Sources and provenance')
 d.p('<b>Assessment status</b>')
 d.p('All 30 questions, their numerical data, solutions, scoring criteria, and diagrams were authored for this diagnostic. The review entries on each solution page are conceptual alignments and reading recommendations, not claims that a question reproduces a source exercise. Therefore no source exercise number applies. No third-party illustrations are reproduced.')
 d.p('<b>The Art of Problem Solving, Volume 1: The Basics</b>')
 d.p('Sandor Lehoczky and Richard Rusczyk, seventh edition, printed 2006 (verified on the copyright page). Local library copy: “The art of problem solving. Volume 1, The basics ( PDFDrive ).pdf.” Use the section titles and printed page numbers listed in the review routes; this scan places printed page 84 at PDF page 98. Chapters 9–18 supply the main elementary geometry coverage.')
 d.p('<b>How to Solve It</b>')
 d.p('G. Polya, second edition, Doubleday Anchor Books (edition verified on scanned title page). Local 29-page scan: “PolyaHowToSolveIt.pdf.” The contents and problem-solving list are scanned images. The four-stage framework—understand, plan, carry out, look back—shapes the interpretation/setup/checking criteria; the scanned contents list Four phases (p. 5), Understanding the problem (p. 6), Devising a plan (p. 8), and Carrying out the plan (p. 12). Use the “How To Solve It” list for strategy review. This local excerpt is not a full searchable copy.')
 d.p('<b>How to Think Like a Mathematician</b>')
 d.p('Kevin Houston. Local manuscript dated February 28, 2008 on its title page: “2-kevin-houston-how-to-think-like-a-mathematician.pdf”; no commercial edition is inferred. Verified contents: Chapters 2–4, Reading/Writing mathematics (pp. 19, 26, 39); Chapter 5, How to solve problems (p. 45); Chapter 12, Examples and counterexamples (p. 92); Chapter 34, True understanding (p. 246). PDF page numbers are printed page + 2. These inform concise explanation, hypothesis checking, error analysis, and unfamiliar-context transfer.')
 d.new('Sources and provenance - continued')
 d.p('<b>The Art and Craft of Problem Solving</b>')
 d.p('Paul Zeitz, second edition, Wiley, 2007 (verified on the title and copyright pages; the local filename includes 2006). Verified source sections: §2.2 Strategies for Getting Started (p. 25), §2.4 Other Important Strategies, especially Draw a Picture! (p. 53); Chapter 8 Geometry for Americans, §§8.2–8.4 (pp. 258–295). Printed page 261 is PDF page 278. Geometry reasoning, auxiliary structure, and area/similarity tactics inform the advanced-transfer tasks.')
 d.p('<b>Treks into Intuitive Geometry: The World of Polygons and Polyhedra</b>')
 d.p('Jin Akiyama and Kiyoko Matsunaga, second edition, Springer, 2024. The local title contains “Treks into Intuitive Geometry.” Chapter 10 §4, Eleven Types of e-Nets of a Cube (printed pp. 407–413), was used for the unfolding/surface-interpretation perspective. The cube-net figure page was visually checked because some body text has a broken PDF character map. It is enrichment, not an assumed prerequisite for the box and cylinder items.')
 d.p('<b>Vault geometry and trig notes</b>')
 d.p('Under 16 - Mathematics/Trigonometry: Section 2.2 - Radian Measure (the Converting section only); geometry-trigonometry-interpretation-practice.md, especially questions 3, 8, 10, and 15. The worksheet provides useful modeling and exact-expression conventions. For special-triangle ratios, use AoPS §11.7. The new test does not reproduce the existing worksheet.')
 d.p('<b>Limits of inference</b>')
 d.p('The diagnostic samples the requested topics. It does not assess every result in these books, compass-and-straightedge construction, formal proof fluency, advanced trigonometry, or calculus. A low closed-book score may reflect formula retrieval as well as conceptual gaps; use the written work and a short follow-up conversation to separate them.')
 d.save()

def score_sheet(d,qs):
 d.p('A = attempted; S = seen/skipped; N = not reached. Confidence 0–3. Use C/D/S/J/A/U error codes; add FT for follow-through. Status S and strategy code S are separate columns.',SMALL)
 rows=[['Q / level','Topic','Score /10','Status','Conf.','Error / missed subskill']]
 for q in qs:rows.append([f"{q['n']} / {q['level']}",q['topic'],'______','____','____','________________________'])
 d.table(rows,[55,96,68,48,48,213],8.5)
 d.p('Subtotal: ______ / 150    Not reached: ______    Seen/skipped: ______')
 d.p('Repeated error pattern: ______________________________________________')
 d.p('___________________________________________________________________')
 d.p('High-confidence errors to revisit: _______________________________________')

if __name__=='__main__':
 validate_data();student_pdf();grader_pdf()
 (Path(__file__).parent/'assessment_manifest.json').write_text(json.dumps({'questions':QUESTIONS,'references':REFERENCES},ensure_ascii=False,indent=2),encoding='utf-8')
 print('Built both PDFs; 30 items; 300 points; difficulty F/S/A = 10/14/6.')

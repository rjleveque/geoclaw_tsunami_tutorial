from pylab import *
from clawpack.geoclaw import kmltools

def make_tile_text(y2, x1):
    y1 = y2 - 0.25
    x2 = x1 + 0.25
    extent = [x1,x2,y1,y2]
    y2a = int(floor(y2))
    y2b = int(mod(y2,1)*100)
    if y2b==0: y2b = '00'
    x1a = int(floor(abs(x1)))
    x1b = int(mod(abs(x1),1)*100)
    if x1b==0: x1b = '00'
    #print('+++ x1 = %.2f, x1a = %s, x1b = %s' % (x1,x1a,x1b))
    name = 'n%ix%s_w%ix%s' % (y2a,y2b,x1a,x1b)
    #kmltools.box2kml(extent, fname=name+'.kml', name=name,
    #                color='FFFFFF',width=1)

    mapping = {}
    mapping['x1'] = x1
    mapping['x2'] = x2
    mapping['y1'] = y1
    mapping['y2'] = y2
    mapping['elev'] = 0.
    mapping['name'] = name
    mapping['desc'] = "  x1 = %s, x2 = %s\n" \
                            % (kmltools.f2s(x1),kmltools.f2s(x2)) \
                    + "  y1 = %s, y2 = %s" % (kmltools.f2s(y1),kmltools.f2s(y2))
    mapping['color'] = 'w'
    mapping['width'] = 2

    tile_text = kmltools.kml_region(mapping)

    return tile_text


kml_text = kmltools.kml_header('NCEI tiles in Cascadia')

for y2 in arange(40.5, 48.6, 0.25):
    for x1 in arange(-125, -123.7, 0.25):
        tile_text = make_tile_text(y2,x1)
        kml_text = kml_text + tile_text

kml_text = kml_text + kmltools.kml_footer()
fname = 'ncei_tile_edges_Cascadia.kml'
kml_file = open(fname,'w')
kml_file.write(kml_text)
print('Created ',fname)

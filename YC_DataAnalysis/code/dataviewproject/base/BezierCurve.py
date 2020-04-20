import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def BezierCurveShow(pathList =[(0, 0), (1, 0), (1, 1), (0, 0)],plotx = [0.75],ploty = [0.25]):
    Path = mpath.Path

    fig, ax = plt.subplots()
    pp1 = mpatches.PathPatch(
        Path(pathList,
             [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
        fc="none", transform=ax.transData)

    ax.add_patch(pp1)
    ax.plot(plotx, ploty, "ro")
    ax.set_title('The red point should be on the path')
    plt.show()

def BezierCurveJPG(pathList =[(0, 0), (1, 0), (1, 1), (0, 0)],plotx = [0.75],ploty = [0.25],
                   savePath = 'BezierCurveJPG.png'):

    import matplotlib
    matplotlib.use('Agg')
    from matplotlib.pyplot import savefig


    Path = mpath.Path

    fig, ax = plt.subplots()
    pp1 = mpatches.PathPatch(
        Path(pathList,
             [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
        fc="none", transform=ax.transData)

    ax.add_patch(pp1)
    ax.plot(plotx, ploty, "ro")
    ax.set_title('The red point should be on the path')
    #plt.show()
    savefig(savePath)

if __name__ =='__main__':  #测试当前类
    BezierCurveJPG()
    #BezierCurveShow([(1, 0), (1, 1), (1, 1), (0, 0)],[0.7],[0.3])

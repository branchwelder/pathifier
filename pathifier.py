class Mark:
    def __init__(self):
        self.geometry = ""
        self.attributes = {}

    def compile(self, **kwargs):
        return self.path.format(**kwargs)


class Circle(Mark):
    def __init__(self):
        path = "M cx, cy m -r, 0 a r,r 0 1,0 (r * 2),0 a r,r 0 1,0 -(r * 2),0"


class Move(Mark):
    path = "m {x},{y}"


class Line(Mark):
    path = "l {dx},{dy}"


class Close(Mark):
    path = "z"


class Heart(Mark):
    def __init__(self):
        path = "M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z"


class Pathifier:
    def __init__(self, width=100, height=100):
        self.marks = []
        self.width = width
        self.height = height

    def addMark(self, mark: Mark, **kwargs):
        self.marks.append(mark.compile(**kwargs))

    def makeSVG(self):
        svg = '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">{contents}</svg>'
        path = '<path d="{d}" />'
        contents = path.format(d=" ".join(self.marks))
        compiled = svg.format(contents=contents)
        with open("test.svg", "w") as f:
            f.write(compiled)

    def makeTemplate(self):
        pass


if __name__ == "__main__":
    p = Pathifier()
    p.addMark(Move(), x=10, y=10)
    p.addMark(Line(), dx=10, dy=15)
    p.addMark(Line(), dx=-10, dy=0)
    p.addMark(Line(), dx=10, dy=-15)
    p.addMark(Close())
    p.makeSVG()

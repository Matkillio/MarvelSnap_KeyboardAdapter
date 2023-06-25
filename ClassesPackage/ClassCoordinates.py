import Helpers.CoordinatesConverter as CoordinatesConverter

class Coordinates:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

Coordinate00 = Coordinates(956, 971)
Coordinate10 = Coordinates(901, 969)
Coordinate11 = Coordinates(1020, 964)
Coordinate20 = Coordinates(841, 970)
Coordinate21 = Coordinates(954, 970)
Coordinate22 = Coordinates(1067, 971)
Coordinate30 = Coordinates(794, 980)
Coordinate31 = Coordinates(922, 975)
Coordinate32 = Coordinates(1012, 978)
Coordinate33 = Coordinates(1120, 983)
Coordinate40 = Coordinates(748, 989)
Coordinate41 = Coordinates(850, 977)
Coordinate42 = Coordinates(957, 972)
Coordinate43 = Coordinates(1059, 988)
Coordinate44 = Coordinates(1171, 981)
Coordinate50 = Coordinates(740, 989)
Coordinate51 = Coordinates(825, 978)
Coordinate52 = Coordinates(912, 978)
Coordinate53 = Coordinates(1007, 979)
Coordinate54 = Coordinates(1095, 980)
Coordinate55 = Coordinates(1186, 984)
Coordinate60 = Coordinates(723, 989)
Coordinate61 = Coordinates(794, 978)
Coordinate62 = Coordinates(877, 971)
Coordinate63 = Coordinates(955, 979)
Coordinate64 = Coordinates(1031, 978)
Coordinate65 = Coordinates(1107, 980)
Coordinate66 = Coordinates(1185, 991)

MatrixCoordinates = [   [Coordinate00, 0, 0, 0, 0, 0, 0],
                        [Coordinate10, Coordinate11, 0, 0, 0, 0, 0],
                        [Coordinate20, Coordinate21, Coordinate22, 0, 0, 0, 0],
                        [Coordinate30, Coordinate31, Coordinate32, Coordinate33, 0, 0, 0],
                        [Coordinate40, Coordinate41, Coordinate42, Coordinate43, Coordinate44, 0, 0],
                        [Coordinate50, Coordinate51, Coordinate52, Coordinate53, Coordinate54, Coordinate55, 0],
                        [Coordinate60, Coordinate61, Coordinate62, Coordinate63, Coordinate64, Coordinate65, Coordinate66]
                    ]


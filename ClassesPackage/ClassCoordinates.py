import Helpers.CoordinatesConverter as CoordinatesConverter

cc = CoordinatesConverter.CoordinatesConverter()

class Coordinates:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

Coordinate00 = Coordinates(cc.ConvertedX(956),cc.ConvertedY(971))
Coordinate10 = Coordinates(cc.ConvertedX(901),cc.ConvertedY(969))
Coordinate11 = Coordinates(cc.ConvertedX(1020),cc.ConvertedY(964))
Coordinate20 = Coordinates(cc.ConvertedX(841),cc.ConvertedY(970))
Coordinate21 = Coordinates(cc.ConvertedX(954),cc.ConvertedY(970))
Coordinate22 = Coordinates(cc.ConvertedX(1067),cc.ConvertedY(971))
Coordinate30 = Coordinates(cc.ConvertedX(794),cc.ConvertedY(980))
Coordinate31 = Coordinates(cc.ConvertedX(922),cc.ConvertedY(975))
Coordinate32 = Coordinates(cc.ConvertedX(1012),cc.ConvertedY(978))
Coordinate33 = Coordinates(cc.ConvertedX(1120),cc.ConvertedY(983))
Coordinate40 = Coordinates(cc.ConvertedX(748),cc.ConvertedY(989))
Coordinate41 = Coordinates(cc.ConvertedX(850),cc.ConvertedY(977))
Coordinate42 = Coordinates(cc.ConvertedX(957),cc.ConvertedY(972))
Coordinate43 = Coordinates(cc.ConvertedX(1059),cc.ConvertedY(988))
Coordinate44 = Coordinates(cc.ConvertedX(1171),cc.ConvertedY(981))
Coordinate50 = Coordinates(cc.ConvertedX(740),cc.ConvertedY(989))
Coordinate51 = Coordinates(cc.ConvertedX(825),cc.ConvertedY(978))
Coordinate52 = Coordinates(cc.ConvertedX(912),cc.ConvertedY(978))
Coordinate53 = Coordinates(cc.ConvertedX(1007),cc.ConvertedY(979))
Coordinate54 = Coordinates(cc.ConvertedX(1095),cc.ConvertedY(980))
Coordinate55 = Coordinates(cc.ConvertedX(1186),cc.ConvertedY(984))
Coordinate60 = Coordinates(cc.ConvertedX(723),cc.ConvertedY(989))
Coordinate61 = Coordinates(cc.ConvertedX(794),cc.ConvertedY(978))
Coordinate62 = Coordinates(cc.ConvertedX(877),cc.ConvertedY(971))
Coordinate63 = Coordinates(cc.ConvertedX(955),cc.ConvertedY(979))
Coordinate64 = Coordinates(cc.ConvertedX(1031),cc.ConvertedY(978))
Coordinate65 = Coordinates(cc.ConvertedX(1107),cc.ConvertedY(980))
Coordinate66 = Coordinates(cc.ConvertedX(1185),cc.ConvertedY(991))

MatrixCoordinates = [   
                        [Coordinate00, 0, 0, 0, 0, 0, 0],
                        [Coordinate10, Coordinate11, 0, 0, 0, 0, 0],
                        [Coordinate20, Coordinate21, Coordinate22, 0, 0, 0, 0],
                        [Coordinate30, Coordinate31, Coordinate32, Coordinate33, 0, 0, 0],
                        [Coordinate40, Coordinate41, Coordinate42, Coordinate43, Coordinate44, 0, 0],
                        [Coordinate50, Coordinate51, Coordinate52, Coordinate53, Coordinate54, Coordinate55, 0],
                        [Coordinate60, Coordinate61, Coordinate62, Coordinate63, Coordinate64, Coordinate65, Coordinate66]
                    ]


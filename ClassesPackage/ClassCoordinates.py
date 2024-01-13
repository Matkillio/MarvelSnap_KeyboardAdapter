import Helpers.CoordinatesConverter as CoordinatesConverter

cc = CoordinatesConverter.CoordinatesConverter()

class Coordinates:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

Coordinate00 = Coordinates(cc.ConvertedX(950), cc.ConvertedY(1035))
Coordinate10 = Coordinates(cc.ConvertedX(865), cc.ConvertedY(1029))
Coordinate11 = Coordinates(cc.ConvertedX(1027), cc.ConvertedY(1036))
Coordinate20 = Coordinates(cc.ConvertedX(794), cc.ConvertedY(1035))
Coordinate21 = Coordinates(cc.ConvertedX(951), cc.ConvertedY(1032))
Coordinate22 = Coordinates(cc.ConvertedX(1103), cc.ConvertedY(1035))
Coordinate30 = Coordinates(cc.ConvertedX(706), cc.ConvertedY(1030))
Coordinate31 = Coordinates(cc.ConvertedX(862), cc.ConvertedY(1029))
Coordinate32 = Coordinates(cc.ConvertedX(1033), cc.ConvertedY(1030))
Coordinate33 = Coordinates(cc.ConvertedX(1181), cc.ConvertedY(1040))
Coordinate40 = Coordinates(cc.ConvertedX(638), cc.ConvertedY(1030))
Coordinate41 = Coordinates(cc.ConvertedX(794), cc.ConvertedY(1035))
Coordinate42 = Coordinates(cc.ConvertedX(940), cc.ConvertedY(1033))
Coordinate43 = Coordinates(cc.ConvertedX(1096), cc.ConvertedY(1024))
Coordinate44 = Coordinates(cc.ConvertedX(1262), cc.ConvertedY(1031))
Coordinate50 = Coordinates(cc.ConvertedX(570), cc.ConvertedY(1035))
Coordinate51 = Coordinates(cc.ConvertedX(722), cc.ConvertedY(1038))
Coordinate52 = Coordinates(cc.ConvertedX(884), cc.ConvertedY(1033))
Coordinate53 = Coordinates(cc.ConvertedX(1031), cc.ConvertedY(1031))
Coordinate54 = Coordinates(cc.ConvertedX(1173), cc.ConvertedY(1040))
Coordinate55 = Coordinates(cc.ConvertedX(1329), cc.ConvertedY(1044))
Coordinate60 = Coordinates(cc.ConvertedX(472), cc.ConvertedY(1040))
Coordinate61 = Coordinates(cc.ConvertedX(624), cc.ConvertedY(1042))
Coordinate62 = Coordinates(cc.ConvertedX(790), cc.ConvertedY(1028))
Coordinate63 = Coordinates(cc.ConvertedX(950), cc.ConvertedY(1029))
Coordinate64 = Coordinates(cc.ConvertedX(1103), cc.ConvertedY(1029))
Coordinate65 = Coordinates(cc.ConvertedX(1256), cc.ConvertedY(1023))
Coordinate66 = Coordinates(cc.ConvertedX(1420), cc.ConvertedY(1038))

MatrixCoordinates = [   
                        [Coordinate00, 0, 0, 0, 0, 0, 0],
                        [Coordinate10, Coordinate11, 0, 0, 0, 0, 0],
                        [Coordinate20, Coordinate21, Coordinate22, 0, 0, 0, 0],
                        [Coordinate30, Coordinate31, Coordinate32, Coordinate33, 0, 0, 0],
                        [Coordinate40, Coordinate41, Coordinate42, Coordinate43, Coordinate44, 0, 0],
                        [Coordinate50, Coordinate51, Coordinate52, Coordinate53, Coordinate54, Coordinate55, 0],
                        [Coordinate60, Coordinate61, Coordinate62, Coordinate63, Coordinate64, Coordinate65, Coordinate66]
                    ]


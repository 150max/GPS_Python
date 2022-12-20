class Cidade:
    def __init__(self):
        print('*'*10 + ' Foi iniciada a classe Cidade ' + '*'*10)

    def CidadesVizinhas(self):
        vizinhos = {
            'Aveiro': {'Porto':68, 'Viseu': 95, 'Coimbra':68, 'Leiria': 115},
            'Braga': {'Viana do Castelo': 48, 'Vila Real': 106, 'Porto':53},
            'Braganca': {'Vila Real': 137, 'Guarda':202},
            'Beja': {'Evora': 78, 'Faro':152, 'Setubal':142},
            'Castelo Branco': {'Coimbra':159,'Guarda':106,'Portalegre':80,'Evora':203},
            'Coimbra': {'Viseu':96,'Leiria':67,'Aveiro':68,'Castelo Branco':159},
            'Evora': {'Lisboa':150,'Santarem':117,'Portalegre':131,'Setubal':103,'Beja':78,'Castelo Branco':203},
            'Faro':  {'Setubal': 249,'Lisboa':299,'Beja':152},
            'Guarda': {'Vila Real':157,'Viseu':85,'Braganca':202,'Castelo Branco':106},
            'Leiria': {'Lisboa':129,'Santarem':70,'Aveiro':115,'Coimbra':67},
            'Lisboa': {'Santarem':78,'Setubal':50,'Evora':150,'Faro':299,'Leiria':129},
            'Portalegre': {'Castelo Branco':80,'Evora':131},
            'Porto': {'Viana do Castelo':71,'Vila Real':116,'Viseu':133, 'Aveiro': 68,'Braga':53},
            'Santarem': {'Evora':117,'Leiria':70,'Lisboa':78},
            'Setubal': {'Beja':142,'Evora':103,'Faro':249,'Lisboa':50},
            'Viana do Castelo': {'Braga':48,'Porto':71},
            'Vila Real': {'Viseu':110,'Braga':106,'Braganca':137, 'Guarda':157,'Porto':116},
            'Viseu': {'Aveiro':95,'Coimbra':96,'Guarda':85,'Porto':133,'Vila Real':110}
        }
        return vizinhos

    def LinhaReta(self):
        linha = {
            'Aveiro': ['Porto', 'Viseu', 'Coimbra', 'Leiria'],
            'Braga': ['Viana do Castelo', 'Vila Real', 'Porto'],
            'Braganca': ['Vila Real', 'Guarda'],
            'Beja': ['Evora', 'Faro', 'Setubal'],
            'Castelo Branco': ['Coimbra', 'Guarda', 'Portalegre', 'Evora'],
            'Coimbra': ['Viseu', 'Leiria', 'Aveiro', 'Castelo Branco'],
            'Evora': ['Lisboa', 'Santarem', 'Portalegre', 'Setubal', 'Beja', 'Castelo Branco'],
            'Faro': ['Setubal', 'Lisboa', 'Beja'],
            'Guarda': ['Vila Real', 'Viseu', 'Braganca', 'Castelo Branco'],
            'Leiria': ['Lisboa', 'Santarem', 'Aveiro', 'Coimbra'],
            'Lisboa': ['Santarem', 'Setubal', 'Evora', 'Faro', 'Leiria'],
            'Porto': ['Viana do Castelo', 'Vila Real', 'Viseu', 'Aveiro', 'Braga'],
            'Vila Real': ['Viseu', 'Braga', 'Braganca', 'Guarda', 'Porto'],
            'Viseu': ['Aveiro', 'Guarda', 'Porto', 'Vila Real', 'Coimbra'],
            'Setubal': ['Beja', 'Evora', 'Faro', 'Lisboa'],
            'Viana do Castelo': ['Braga', 'Porto'],
            'Santarem': ['Evora', 'Leiria', 'Lisboa'],
            'Portalegre': ['Castelo Branco', 'Evora']
        }
        return linha

    def DistanciaReta(self):
        distancia = {
            ('Faro', 'Aveiro'): 366,
            ('Faro', 'Braga'): 454,
            ('Faro', 'Braganca'): 487,
            ('Faro', 'Beja'): 99,
            ('Faro', 'Castelo Branco'): 280,
            ('Faro', 'Coimbra'): 319,
            ('Faro', 'Evora'): 157,
            ('Faro', 'Faro'): 0,
            ('Faro', 'Guarda'): 352,
            ('Faro', 'Leiria'): 278,
            ('Faro', 'Lisboa'): 195,
            ('Faro', 'Portalegre'): 228,
            ('Faro', 'Porto'): 418,
            ('Faro', 'Santarem'): 231,
            ('Faro', 'Setubal'): 168,
            ('Faro', 'Viana'): 473,
            ('Faro', 'Vila Real'): 429,
            ('Faro', 'Viseu'): 363,
            ('Aveiro', 'Faro'): 366,
            ('Braga', 'Faro'): 454,
            ('Braganca', 'Faro'): 487,
            ('Beja', 'Faro'): 99,
            ('Castelo Branco', 'Faro'): 280,
            ('Coimbra', 'Faro'): 319,
            ('Evora', 'Faro'): 157,
            ('Faro', 'Faro'): 0,
            ('Guarda', 'Faro'): 352,
            ('Leiria', 'Faro'): 278,
            ('Lisboa', 'Faro'): 195,
            ('Portalegre', 'Faro'): 228,
            ('Porto', 'Faro'): 418,
            ('Santarem', 'Faro'): 231,
            ('Setubal', 'Faro'): 168,
            ('Viana do Castelo', 'Faro'): 473,
            ('Vila Real', 'Faro'): 429,
            ('Viseu', 'Faro'): 363

        }
        return distancia


    def Peso(self):
        pesos = {
            ('Aveiro', 'Porto'): 68,
            ('Aveiro', 'Viseu'): 95,
            ('Aveiro', 'Coimbra'): 68,
            ('Aveiro', 'Leiria'): 115,

            ('Braga', 'Viana do Castelo'): 48,
            ('Braga', 'Vila Real'): 106,
            ('Braga', 'Porto'): 53,

            ('Braganca', 'Vila Real'): 137,
            ('Braganca', 'Guarda'): 202,

            ('Beja', 'Evora'): 78,
            ('Beja', 'Faro'): 152,
            ('Beja', 'Setubal'): 142,

            ('Castelo Branco', 'Coimbra'): 159,
            ('Castelo Branco', 'Guarda'): 106,
            ('Castelo Branco', 'Portalegre'): 80,
            ('Castelo Branco', 'Evora'): 203,

            ('Coimbra', 'Viseu'): 96,
            ('Coimbra', 'Leiria'): 67,
            ('Coimbra', 'Aveiro'): 68,
            ('Coimbra', 'Castelo Branco'): 159,

            ('Evora','Lisboa'): 150,
            ('Evora','Santarem'): 117,
            ('Evora','Portalegre'): 131,
            ('Evora','Setubal'): 103,
            ('Evora','Beja'): 78,
            ('Evora','Castelo Branco'): 203,

            ('Faro', 'Setubal'): 249,
            ('Faro', 'Lisboa'): 299,
            ('Faro', 'Beja'): 152,

            ('Guarda', 'Vila Real'): 157,
            ('Guarda', 'Viseu'): 85,
            ('Guarda', 'Braganca'): 202,
            ('Guarda', 'Castelo Branco'): 106,

            ('Leiria', 'Lisboa'): 129,
            ('Leiria', 'Santarem'): 70,
            ('Leiria', 'Aveiro'): 115,
            ('Leiria', 'Coimbra'): 67,

            ('Lisboa', 'Santarem'): 78,
            ('Lisboa', 'Setubal'): 50,
            ('Lisboa', 'Evora'): 150,
            ('Lisboa', 'Faro'): 299,
            ('Lisboa', 'Leiria'): 129,

            ('Porto', 'Viana do Castelo'): 71,
            ('Porto', 'Vila Real'): 116,
            ('Porto', 'Viseu'): 133,
            ('Porto', 'Aveiro'): 68,
            ('Porto', 'Braga'): 53,

            ('Vila Real', 'Viseu'): 110,
            ('Vila Real', 'Braga'): 106,
            ('Vila Real', 'Braganca'): 137,
            ('Vila Real', 'Guarda'): 157,
            ('Vila Real', 'Porto'): 116,

            ('Viseu', 'Aveiro'): 95,
            ('Viseu', 'Coimbra'): 96,
            ('Viseu', 'Guarda'): 85,
            ('Viseu', 'Porto'): 133,
            ('Viseu', 'Vila Real'): 110,
            
            ('Setubal', 'Beja'): 142,
            ('Setubal', 'Evora'): 103,
            ('Setubal', 'Faro'): 249,
            ('Setubal', 'Lisboa'): 50,

            ('Santarem', 'Evora'): 117,
            ('Santarem', 'Leiria'): 70,
            ('Santarem', 'Lisboa'): 78,

            ('Viana do Castelo', 'Braga'): 48,
            ('Viana do Castelo', 'Porto'): 71,
            
            ('Portalegre', 'Castelo Branco'): 80,
            ('Portalegre', 'Evora'): 131

        }
        return pesos
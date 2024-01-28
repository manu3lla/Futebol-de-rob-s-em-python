from math import sqrt
import matplotlib.pyplot as plt

# função para formatar a tabela com as informações da trajetória da bola em listas
def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:

        conteudo = arquivo.read()
        numeros = conteudo.split('\n')
        numeros_formatados = []

        for numero in numeros:
            numero_formatado = numero.replace(',', '.') + ','
            numeros_formatados.append(numero_formatado)

        resultado = ''.join(numeros_formatados)

        print(resultado)

# uso da função
# processar_arquivo('numerosY')
# processar_arquivo('numerosX')
# processar_arquivo('tempo')

t = [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38,
     0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78,
     0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1.02, 1.04, 1.06, 1.08, 1.1, 1.12, 1.14, 1.16, 1.18,
     1.2, 1.22, 1.24, 1.26, 1.28, 1.3, 1.32, 1.34, 1.36, 1.38, 1.4, 1.42, 1.44, 1.46, 1.48, 1.5, 1.52, 1.54, 1.56, 1.58,
     1.6, 1.62, 1.64, 1.66, 1.68, 1.7, 1.72, 1.74, 1.76, 1.78, 1.8, 1.82, 1.84, 1.86, 1.88, 1.9, 1.92, 1.94, 1.96, 1.98,
     2, 2.02, 2.04, 2.06, 2.08, 2.1, 2.12, 2.14, 2.16, 2.18, 2.2, 2.22, 2.24, 2.26, 2.28, 2.3, 2.32, 2.34, 2.36, 2.38,
     2.4, 2.42, 2.44, 2.46, 2.48, 2.5, 2.52, 2.54, 2.56, 2.58, 2.6, 2.62, 2.64, 2.66, 2.68, 2.7, 2.72, 2.74, 2.76, 2.78,
     2.8, 2.82, 2.84, 2.86, 2.88, 2.9, 2.92, 2.94, 2.96, 2.98, 3, 3.02, 3.04, 3.06, 3.08, 3.1, 3.12, 3.14, 3.16, 3.18,
     3.2, 3.22, 3.24, 3.26, 3.28, 3.3, 3.32, 3.34, 3.36, 3.38, 3.4, 3.42, 3.44, 3.46, 3.48, 3.5, 3.52, 3.54, 3.56, 3.58,
     3.6, 3.62, 3.64, 3.66, 3.68, 3.7, 3.72, 3.74, 3.76, 3.78, 3.8, 3.82, 3.84, 3.86, 3.88, 3.9, 3.92, 3.94, 3.96, 3.98,
     4, 4.02, 4.04, 4.06, 4.08, 4.1, 4.12, 4.14, 4.16, 4.18, 4.2, 4.22, 4.24, 4.26, 4.28, 4.3, 4.32, 4.34, 4.36, 4.38,
     4.4, 4.42, 4.44, 4.46, 4.48, 4.5, 4.52, 4.54, 4.56, 4.58, 4.6, 4.62, 4.64, 4.66, 4.68, 4.7, 4.72, 4.74, 4.76, 4.78,
     4.8, 4.82, 4.84, 4.86, 4.88, 4.9, 4.92, 4.94, 4.96, 4.98, 5, 5.02, 5.04, 5.06, 5.08, 5.1, 5.12, 5.14, 5.16, 5.18,
     5.2, 5.22, 5.24, 5.26, 5.28, 5.3, 5.32, 5.34, 5.36, 5.38, 5.4, 5.42, 5.44, 5.46, 5.48, 5.5, 5.52, 5.54, 5.56, 5.58,
     5.6, 5.62, 5.64, 5.66, 5.68, 5.7, 5.72, 5.74, 5.76, 5.78, 5.8, 5.82, 5.84, 5.86, 5.88, 5.9, 5.92, 5.94, 5.96, 5.98,
     6, 6.02, 6.04, 6.06, 6.08, 6.1, 6.12, 6.14, 6.16, 6.18, 6.2, 6.22, 6.24, 6.26, 6.28, 6.3, 6.32, 6.34, 6.36, 6.38,
     6.4, 6.42, 6.44, 6.46, 6.48, 6.5, 6.52, 6.54, 6.56, 6.58, 6.6, 6.62, 6.64, 6.66, 6.68, 6.7, 6.72, 6.74, 6.76, 6.78,
     6.8, 6.82, 6.84, 6.86, 6.88, 6.9, 6.92, 6.94, 6.96, 6.98, 7, 7.02, 7.04, 7.06, 7.08, 7.1, 7.12, 7.14, 7.16, 7.18,
     7.2, 7.22, 7.24, 7.26, 7.28, 7.3, 7.32, 7.34, 7.36, 7.38, 7.4, 7.42, 7.44, 7.46, 7.48, 7.5, 7.52, 7.54, 7.56, 7.58,
     7.6, 7.62, 7.64, 7.66, 7.68, 7.7, 7.72, 7.74, 7.76, 7.78, 7.8, 7.82, 7.84, 7.86, 7.88, 7.9, 7.92, 7.94, 7.96, 7.98,
     8, 8.02, 8.04, 8.06, 8.08, 8.1, 8.12, 8.14, 8.16, 8.18, 8.2, 8.22, 8.24, 8.26, 8.28, 8.3, 8.32, 8.34, 8.36, 8.38,
     8.4, 8.42, 8.44, 8.46, 8.48, 8.5, 8.52, 8.54, 8.56, 8.58, 8.6, 8.62, 8.64, 8.66, 8.68, 8.7, 8.72, 8.74, 8.76, 8.78,
     8.8, 8.82, 8.84, 8.86, 8.88, 8.9, 8.92, 8.94, 8.96, 8.98, 9, 9.02, 9.04, 9.06, 9.08, 9.1, 9.12, 9.14, 9.16, 9.18,
     9.2, 9.22, 9.24, 9.26, 9.28, 9.3, 9.32, 9.34, 9.36, 9.38, 9.4, 9.42, 9.44, 9.46, 9.48, 9.5, 9.52, 9.54, 9.56, 9.58,
     9.6, 9.62, 9.64, 9.66, 9.68, 9.7, 9.72, 9.74, 9.76, 9.78, 9.8, 9.82, 9.84, 9.86, 9.88, 9.9, 9.92, 9.94, 9.96, 9.98,
     10, 10.02, 10.04, 10.06, 10.08, 10.1, 10.12, 10.14, 10.16, 10.18, 10.2, 10.22, 10.24, 10.26, 10.28, 10.3, 10.32,
     10.34, 10.36, 10.38, 10.4, 10.42, 10.44, 10.46, 10.48, 10.5, 10.52, 10.54, 10.56, 10.58, 10.6, 10.62, 10.64, 10.66,
     10.68, 10.7, 10.72, 10.74, 10.76, 10.78, 10.8, 10.82, 10.84, 10.86, 10.88, 10.9, 10.92, 10.94, 10.96, 10.98, 11,
     11.02, 11.04, 11.06, 11.08, 11.1, 11.12, 11.14, 11.16, 11.18, 11.2, 11.22, 11.24, 11.26, 11.28, 11.3, 11.32, 11.34,
     11.36, 11.38, 11.4, 11.42, 11.44, 11.46, 11.48, 11.5, 11.52, 11.54, 11.56, 11.58, 11.6, 11.62, 11.64, 11.66, 11.68,
     11.7, 11.72, 11.74, 11.76, 11.78, 11.8, 11.82, 11.84, 11.86, 11.88, 11.9, 11.92, 11.94, 11.96, 11.98, 12, 12.02,
     12.04, 12.06, 12.08, 12.1, 12.12, 12.14, 12.16, 12.18, 12.2, 12.22, 12.24, 12.26, 12.28, 12.3, 12.32, 12.34, 12.36,
     12.38, 12.4, 12.42, 12.44, 12.46, 12.48, 12.5, 12.52, 12.54, 12.56, 12.58, 12.6, 12.62, 12.64, 12.66, 12.68, 12.7,
     12.72, 12.74, 12.76, 12.78, 12.8, 12.82, 12.84, 12.86, 12.88, 12.9, 12.92, 12.94, 12.96, 12.98, 13, 13.02, 13.04,
     13.06, 13.08, 13.1, 13.12, 13.14, 13.16, 13.18, 13.2, 13.22, 13.24, 13.26, 13.28, 13.3, 13.32, 13.34, 13.36, 13.38,
     13.4, 13.42, 13.44, 13.46, 13.48, 13.5, 13.52, 13.54, 13.56, 13.58, 13.6, 13.62, 13.64, 13.66, 13.68, 13.7, 13.72,
     13.74, 13.76, 13.78, 13.8, 13.82, 13.84, 13.86, 13.88, 13.9, 13.92, 13.94, 13.96, 13.98, 14, 14.02, 14.04, 14.06,
     14.08, 14.1, 14.12, 14.14, 14.16, 14.18, 14.2, 14.22, 14.24, 14.26, 14.28, 14.3, 14.32, 14.34, 14.36, 14.38, 14.4,
     14.42, 14.44, 14.46, 14.48, 14.5, 14.52, 14.54, 14.56, 14.58, 14.6, 14.62, 14.64, 14.66, 14.68, 14.7, 14.72, 14.74,
     14.76, 14.78, 14.8, 14.82, 14.84, 14.86, 14.88, 14.9, 14.92, 14.94, 14.96, 14.98, 15, 15.02, 15.04, 15.06, 15.08,
     15.1, 15.12, 15.14, 15.16, 15.18, 15.2, 15.22, 15.24, 15.26, 15.28, 15.3, 15.32, 15.34, 15.36, 15.38, 15.4, 15.42,
     15.44, 15.46, 15.48, 15.5, 15.52, 15.54, 15.56, 15.58, 15.6, 15.62, 15.64, 15.66, 15.68, 15.7, 15.72, 15.74, 15.76,
     15.78, 15.8, 15.82, 15.84, 15.86, 15.88, 15.9, 15.92, 15.94, 15.96, 15.98, 16, 16.02, 16.04, 16.06, 16.08, 16.1,
     16.12, 16.14, 16.16, 16.18, 16.2, 16.22, 16.24, 16.26, 16.28, 16.3, 16.32, 16.34, 16.36, 16.38, 16.4, 16.42, 16.44,
     16.46, 16.48, 16.5, 16.52, 16.54, 16.56, 16.58, 16.6, 16.62, 16.64, 16.66, 16.68, 16.7, 16.72, 16.74, 16.76, 16.78,
     16.8, 16.82, 16.84, 16.86, 16.88, 16.9, 16.92, 16.94, 16.96, 16.98, 17, 17.02, 17.04, 17.06, 17.08, 17.1, 17.12,
     17.14, 17.16, 17.18, 17.2, 17.22, 17.24, 17.26, 17.28, 17.3, 17.32, 17.34, 17.36, 17.38, 17.4, 17.42, 17.44, 17.46,
     17.48, 17.5, 17.52, 17.54, 17.56, 17.58, 17.6, 17.62, 17.64, 17.66, 17.68, 17.7, 17.72, 17.74, 17.76, 17.78, 17.8,
     17.82, 17.84, 17.86, 17.88, 17.9, 17.92, 17.94, 17.96, 17.98, 18, 18.02, 18.04, 18.06, 18.08, 18.1, 18.12, 18.14,
     18.16, 18.18, 18.2, 18.22, 18.24, 18.26, 18.28, 18.3, 18.32, 18.34, 18.36, 18.38, 18.4, 18.42, 18.44, 18.46, 18.48,
     18.5, 18.52, 18.54, 18.56, 18.58, 18.6, 18.62, 18.64, 18.66, 18.68, 18.7, 18.72, 18.74, 18.76, 18.78, 18.8, 18.82,
     18.84, 18.86, 18.88, 18.9, 18.92, 18.94, 18.96, 18.98, 19, 19.02, 19.04, 19.06, 19.08, 19.1, 19.12, 19.14, 19.16,
     19.18, 19.2, 19.22, 19.24, 19.26, 19.28, 19.3, 19.32, 19.34, 19.36, 19.38, 19.4, 19.42, 19.44, 19.46, 19.48, 19.5,
     19.52, 19.54, 19.56, 19.58, 19.6, 19.62, 19.64, 19.66, 19.68, 19.7, 19.72, 19.74, 19.76, 19.78, 19.8, 19.82, 19.84,
     19.86, 19.88, 19.9, 19.92, 19.94, 19.96, 19.98, 20]

x = [1, 1.01000004, 1.02000032, 1.03000108, 1.04000256, 1.050005, 1.06000864, 1.07001372, 1.08002048, 1.09002916,
     1.10004, 1.11005324, 1.12006912, 1.13008788, 1.14010976, 1.150135, 1.16016384, 1.17019652, 1.18023328, 1.19027436,
     1.20032, 1.21037044, 1.22042592, 1.23048668, 1.24055296, 1.250625, 1.26070304, 1.27078732, 1.28087808, 1.29097556,
     1.30108, 1.31119164, 1.32131072, 1.33143748, 1.34157216, 1.351715, 1.36186624, 1.37202612, 1.38219488, 1.39237276,
     1.40256, 1.41275684, 1.42296352, 1.43318028, 1.44340736, 1.453645, 1.46389344, 1.47415292, 1.48442368, 1.49470596,
     1.505, 1.51530604, 1.52562432, 1.53595508, 1.54629856, 1.556655, 1.56702464, 1.57740772, 1.58780448, 1.59821516,
     1.60864, 1.61907924, 1.62953312, 1.64000188, 1.65048576, 1.660985, 1.67149984, 1.68203052, 1.69257728, 1.70314036,
     1.71372, 1.72431644, 1.73492992, 1.74556068, 1.75620896, 1.766875, 1.77755904, 1.78826132, 1.79898208, 1.80972156,
     1.82048, 1.83125764, 1.84205472, 1.85287148, 1.86370816, 1.874565, 1.88544224, 1.89634012, 1.90725888, 1.91819876,
     1.92916, 1.94014284, 1.95114752, 1.96217428, 1.97322336, 1.984295, 1.99538944, 2.00650692, 2.01764768, 2.02881196,
     2.04, 2.05121204, 2.06244832, 2.07370908, 2.08499456, 2.096305, 2.10764064, 2.11900172, 2.13038848, 2.14180116,
     2.15324, 2.16470524, 2.17619712, 2.18771588, 2.19926176, 2.210835, 2.22243584, 2.23406452, 2.24572128, 2.25740636,
     2.26912, 2.28086244, 2.29263392, 2.30443468, 2.31626496, 2.328125, 2.34001504, 2.35193532, 2.36388608, 2.37586756,
     2.38788, 2.39992364, 2.41199872, 2.42410548, 2.43624416, 2.448415, 2.46061824, 2.47285412, 2.48512288, 2.49742476,
     2.50976, 2.52212884, 2.53453152, 2.54696828, 2.55943936, 2.571945, 2.58448544, 2.59706092, 2.60967168, 2.62231796,
     2.635, 2.64771804, 2.66047232, 2.67326308, 2.68609056, 2.698955, 2.71185664, 2.72479572, 2.73777248, 2.75078716,
     2.76384, 2.77693124, 2.79006112, 2.80322988, 2.81643776, 2.829685, 2.84297184, 2.85629852, 2.86966528, 2.88307236,
     2.89652, 2.91000844, 2.92353792, 2.93710868, 2.95072096, 2.964375, 2.97807104, 2.99180932, 3.00559008, 3.01941356,
     3.03328, 3.04718964, 3.06114272, 3.07513948, 3.08918016, 3.103265, 3.11739424, 3.13156812, 3.14578688, 3.16005076,
     3.17436, 3.18871484, 3.20311552, 3.21756228, 3.23205536, 3.246595, 3.26118144, 3.27581492, 3.29049568, 3.30522396,
     3.32, 3.33482404, 3.34969632, 3.36461708, 3.37958656, 3.394605, 3.40967264, 3.42478972, 3.43995648, 3.45517316,
     3.47044, 3.48575724, 3.50112512, 3.51654388, 3.53201376, 3.547535, 3.56310784, 3.57873252, 3.59440928, 3.61013836,
     3.62592, 3.64175444, 3.65764192, 3.67358268, 3.68957696, 3.705625, 3.72172704, 3.73788332, 3.75409408, 3.77035956,
     3.78668, 3.80305564, 3.81948672, 3.83597348, 3.85251616, 3.869115, 3.88577024, 3.90248212, 3.91925088, 3.93607676,
     3.95296, 3.96990084, 3.98689952, 4.00395628, 4.02107136, 4.038245, 4.05547744, 4.07276892, 4.09011968, 4.10752996,
     4.125, 4.14253004, 4.16012032, 4.17777108, 4.19548256, 4.213255, 4.23108864, 4.24898372, 4.26694048, 4.28495916,
     4.30304, 4.32118324, 4.33938912, 4.35765788, 4.37598976, 4.394385, 4.41284384, 4.43136652, 4.44995328, 4.46860436,
     4.48732, 4.50610044, 4.52494592, 4.54385668, 4.56283296, 4.581875, 4.60098304, 4.62015732, 4.63939808, 4.65870556,
     4.67808, 4.69752164, 4.71703072, 4.73660748, 4.75625216, 4.775965, 4.79574624, 4.81559612, 4.83551488, 4.85550276,
     4.87556, 4.89568684, 4.91588352, 4.93615028, 4.95648736, 4.976895, 4.99737344, 5.01792292, 5.03854368, 5.05923596,
     5.08, 5.10083604, 5.12174432, 5.14272508, 5.16377856, 5.184905, 5.20610464, 5.22737772, 5.24872448, 5.27014516,
     5.29164, 5.31320924, 5.33485312, 5.35657188, 5.37836576, 5.400235, 5.42217984, 5.44420052, 5.46629728, 5.48847036,
     5.51072, 5.53304644, 5.55544992, 5.57793068, 5.60048896, 5.623125, 5.64583904, 5.66863132, 5.69150208, 5.71445156,
     5.73748, 5.76058764, 5.78377472, 5.80704148, 5.83038816, 5.853815, 5.87732224, 5.90091012, 5.92457888, 5.94832876,
     5.97216, 5.99607284, 6.02006752, 6.04414428, 6.06830336, 6.092545, 6.11686944, 6.14127692, 6.16576768, 6.19034196,
     6.215, 6.23974204, 6.26456832, 6.28947908, 6.31447456, 6.339555, 6.36472064, 6.38997172, 6.41530848, 6.44073116,
     6.46624, 6.49183524, 6.51751712, 6.54328588, 6.56914176, 6.595085, 6.62111584, 6.64723452, 6.67344128, 6.69973636,
     6.72612, 6.75259244, 6.77915392, 6.80580468, 6.83254496, 6.859375, 6.88629504, 6.91330532, 6.94040608, 6.96759756,
     6.99488, 7.02225364, 7.04971872, 7.07727548, 7.10492416, 7.132665, 7.16049824, 7.18842412, 7.21644288, 7.24455476,
     7.27276, 7.30105884, 7.32945152, 7.35793828, 7.38651936, 7.415195, 7.44396544, 7.47283092, 7.50179168, 7.53084796,
     7.56, 7.58924804, 7.61859232, 7.64803308, 7.67757056, 7.707205, 7.73693664, 7.76676572, 7.79669248, 7.82671716,
     7.85684, 7.88706124, 7.91738112, 7.94779988, 7.97831776, 8.008935, 8.03965184, 8.07046852, 8.10138528, 8.13240236,
     8.16352, 8.19473844, 8.22605792, 8.25747868, 8.28900096, 8.320625, 8.35235104, 8.38417932, 8.41611008, 8.44814356,
     8.48028, 8.51251964, 8.54486272, 8.57730948, 8.60986016, 8.642515, 8.67527424, 8.70813812, 8.74110688, 8.77418076,
     8.80736, 8.84064484, 8.87403552, 8.90753228, 8.94113536, 8.974845, 9.00866144, 9.04258492, 9.07661568, 9.11075396,
     9.145, 9.17935404, 9.21381632, 9.24838708, 9.28306656, 9.317855, 9.35275264, 9.38775972, 9.42287648, 9.45810316,
     9.49344, 9.52888724, 9.56444512, 9.60011388, 9.63589376, 9.671785, 9.70778784, 9.74390252, 9.78012928, 9.81646836,
     9.85292, 9.88948444, 9.92616192, 9.96295268, 9.99985696, 10.036875, 10.07400704, 10.11125332, 10.14861408,
     10.18608956, 10.22368, 10.26138564, 10.29920672, 10.33714348, 10.37519616, 10.413365, 10.45165024, 10.49005212,
     10.52857088, 10.56720676, 10.60596, 10.64483084, 10.68381952, 10.72292628, 10.76215136, 10.801495, 10.84095744,
     10.88053892, 10.92023968, 10.96005996, 11, 11.04006004, 11.08024032, 11.12054108, 11.16096256, 11.201505,
     11.24216864, 11.28295372, 11.32386048, 11.36488916, 11.40604, 11.44731324, 11.48870912, 11.53022788, 11.57186976,
     11.613635, 11.65552384, 11.69753652, 11.73967328, 11.78193436, 11.82432, 11.86683044, 11.90946592, 11.95222668,
     11.99511296, 12.038125, 12.08126304, 12.12452732, 12.16791808, 12.21143556, 12.25508, 12.29885164, 12.34275072,
     12.38677748, 12.43093216, 12.475215, 12.51962624, 12.56416612, 12.60883488, 12.65363276, 12.69856, 12.74361684,
     12.78880352, 12.83412028, 12.87956736, 12.925145, 12.97085344, 13.01669292, 13.06266368, 13.10876596, 13.155,
     13.20136604, 13.24786432, 13.29449508, 13.34125856, 13.388155, 13.43518464, 13.48234772, 13.52964448, 13.57707516,
     13.62464, 13.67233924, 13.72017312, 13.76814188, 13.81624576, 13.864485, 13.91285984, 13.96137052, 14.01001728,
     14.05880036, 14.10772, 14.15677644, 14.20596992, 14.25530068, 14.30476896, 14.354375, 14.40411904, 14.45400132,
     14.50402208, 14.55418156, 14.60448, 14.65491764, 14.70549472, 14.75621148, 14.80706816, 14.858065, 14.90920224,
     14.96048012, 15.01189888, 15.06345876, 15.11516, 15.16700284, 15.21898752, 15.27111428, 15.32338336, 15.375795,
     15.42834944, 15.48104692, 15.53388768, 15.58687196, 15.64, 15.69327204, 15.74668832, 15.80024908, 15.85395456,
     15.907805, 15.96180064, 16.01594172, 16.07022848, 16.12466116, 16.17924, 16.23396524, 16.28883712, 16.34385588,
     16.39902176, 16.454335, 16.50979584, 16.56540452, 16.62116128, 16.67706636, 16.73312, 16.78932244, 16.84567392,
     16.90217468, 16.95882496, 17.015625, 17.07257504, 17.12967532, 17.18692608, 17.24432756, 17.30188, 17.35958364,
     17.41743872, 17.47544548, 17.53360416, 17.591915, 17.65037824, 17.70899412, 17.76776288, 17.82668476, 17.88576,
     17.94498884, 18.00437152, 18.06390828, 18.12359936, 18.183445, 18.24344544, 18.30360092, 18.36391168, 18.42437796,
     18.485, 18.54577804, 18.60671232, 18.66780308, 18.72905056, 18.790455, 18.85201664, 18.91373572, 18.97561248,
     19.03764716, 19.09984, 19.16219124, 19.22470112, 19.28736988, 19.35019776, 19.413185, 19.47633184, 19.53963852,
     19.60310528, 19.66673236, 19.73052, 19.79446844, 19.85857792, 19.92284868, 19.98728096, 20.051875, 20.11663104,
     20.18154932, 20.24663008, 20.31187356, 20.37728, 20.44284964, 20.50858272, 20.57447948, 20.64054016, 20.706765,
     20.77315424, 20.83970812, 20.90642688, 20.97331076, 21.04036, 21.10757484, 21.17495552, 21.24250228, 21.31021536,
     21.378095, 21.44614144, 21.51435492, 21.58273568, 21.65128396, 21.72, 21.78888404, 21.85793632, 21.92715708,
     21.99654656, 22.066105, 22.13583264, 22.20572972, 22.27579648, 22.34603316, 22.41644, 22.48701724, 22.55776512,
     22.62868388, 22.69977376, 22.771035, 22.84246784, 22.91407252, 22.98584928, 23.05779836, 23.12992, 23.20221444,
     23.27468192, 23.34732268, 23.42013696, 23.493125, 23.56628704, 23.63962332, 23.71313408, 23.78681956, 23.86068,
     23.93471564, 24.00892672, 24.08331348, 24.15787616, 24.232615, 24.30753024, 24.38262212, 24.45789088, 24.53333676,
     24.60896, 24.68476084, 24.76073952, 24.83689628, 24.91323136, 24.989745, 25.06643744, 25.14330892, 25.22035968,
     25.29758996, 25.375, 25.45259004, 25.53036032, 25.60831108, 25.68644256, 25.764755, 25.84324864, 25.92192372,
     26.00078048, 26.07981916, 26.15904, 26.23844324, 26.31802912, 26.39779788, 26.47774976, 26.557885, 26.63820384,
     26.71870652, 26.79939328, 26.88026436, 26.96132, 27.04256044, 27.12398592, 27.20559668, 27.28739296, 27.369375,
     27.45154304, 27.53389732, 27.61643808, 27.69916556, 27.78208, 27.86518164, 27.94847072, 28.03194748, 28.11561216,
     28.199465, 28.28350624, 28.36773612, 28.45215488, 28.53676276, 28.62156, 28.70654684, 28.79172352, 28.87709028,
     28.96264736, 29.048395, 29.13433344, 29.22046292, 29.30678368, 29.39329596, 29.48, 29.56689604, 29.65398432,
     29.74126508, 29.82873856, 29.916405, 30.00426464, 30.09231772, 30.18056448, 30.26900516, 30.35764, 30.44646924,
     30.53549312, 30.62471188, 30.71412576, 30.803735, 30.89353984, 30.98354052, 31.07373728, 31.16413036, 31.25472,
     31.34550644, 31.43648992, 31.52767068, 31.61904896, 31.710625, 31.80239904, 31.89437132, 31.98654208, 32.07891156,
     32.17148, 32.26424764, 32.35721472, 32.45038148, 32.54374816, 32.637315, 32.73108224, 32.82505012, 32.91921888,
     33.01358876, 33.10816, 33.20293284, 33.29790752, 33.39308428, 33.48846336, 33.584045, 33.67982944, 33.77581692,
     33.87200768, 33.96840196, 34.065, 34.16180204, 34.25880832, 34.35601908, 34.45343456, 34.551055, 34.64888064,
     34.74691172, 34.84514848, 34.94359116, 35.04224, 35.14109524, 35.24015712, 35.33942588, 35.43890176, 35.538585,
     35.63847584, 35.73857452, 35.83888128, 35.93939636, 36.04012, 36.14105244, 36.24219392, 36.34354468, 36.44510496,
     36.546875, 36.64885504, 36.75104532, 36.85344608, 36.95605756, 37.05888, 37.16191364, 37.26515872, 37.36861548,
     37.47228416, 37.576165, 37.68025824, 37.78456412, 37.88908288, 37.99381476, 38.09876, 38.20391884, 38.30929152,
     38.41487828, 38.52067936, 38.626695, 38.73292544, 38.83937092, 38.94603168, 39.05290796, 39.16, 39.26730804,
     39.37483232, 39.48257308, 39.59053056, 39.698705, 39.80709664, 39.91570572, 40.02453248, 40.13357716, 40.24284,
     40.35232124, 40.46202112, 40.57193988, 40.68207776, 40.792435, 40.90301184, 41.01380852, 41.12482528, 41.23606236,
     41.34752, 41.45919844, 41.57109792, 41.68321868, 41.79556096, 41.908125, 42.02091104, 42.13391932, 42.24715008,
     42.36060356, 42.47428, 42.58817964, 42.70230272, 42.81664948, 42.93122016, 43.046015, 43.16103424, 43.27627812,
     43.39174688, 43.50744076, 43.62336, 43.73950484, 43.85587552, 43.97247228, 44.08929536, 44.206345, 44.32362144,
     44.44112492, 44.55885568, 44.67681396, 44.795, 44.91341404, 45.03205632, 45.15092708, 45.27002656, 45.389355,
     45.50891264, 45.62869972, 45.74871648, 45.86896316, 45.98944, 46.11014724, 46.23108512, 46.35225388, 46.47365376,
     46.595285, 46.71714784, 46.83924252, 46.96156928, 47.08412836, 47.20692, 47.32994444, 47.45320192, 47.57669268,
     47.70041696, 47.824375, 47.94856704, 48.07299332, 48.19765408, 48.32254956, 48.44768, 48.57304564, 48.69864672,
     48.82448348, 48.95055616, 49.076865, 49.20341024, 49.33019212, 49.45721088, 49.58446676, 49.71196, 49.83969084,
     49.96765952, 50.09586628, 50.22431136, 50.352995, 50.48191744, 50.61107892, 50.74047968, 50.87011996, 51]

y = [0.5, 0.517992, 0.535968, 0.553928, 0.571872, 0.5898, 0.607712, 0.625608, 0.643488, 0.661352, 0.6792, 0.697032,
     0.714848, 0.732648, 0.750432, 0.7682, 0.785952, 0.803688, 0.821408, 0.839112, 0.8568, 0.874472, 0.892128, 0.909768,
     0.927392, 0.945, 0.962592, 0.980168, 0.997728, 1.015272, 1.0328, 1.050312, 1.067808, 1.085288, 1.102752, 1.1202,
     1.137632, 1.155048, 1.172448, 1.189832, 1.2072, 1.224552, 1.241888, 1.259208, 1.276512, 1.2938, 1.311072, 1.328328,
     1.345568, 1.362792, 1.38, 1.397192, 1.414368, 1.431528, 1.448672, 1.4658, 1.482912, 1.500008, 1.517088, 1.534152,
     1.5512, 1.568232, 1.585248, 1.602248, 1.619232, 1.6362, 1.653152, 1.670088, 1.687008, 1.703912, 1.7208, 1.737672,
     1.754528, 1.771368, 1.788192, 1.805, 1.821792, 1.838568, 1.855328, 1.872072, 1.8888, 1.905512, 1.922208, 1.938888,
     1.955552, 1.9722, 1.988832, 2.005448, 2.022048, 2.038632, 2.0552, 2.071752, 2.088288, 2.104808, 2.121312, 2.1378,
     2.154272, 2.170728, 2.187168, 2.203592, 2.22, 2.236392, 2.252768, 2.269128, 2.285472, 2.3018, 2.318112, 2.334408,
     2.350688, 2.366952, 2.3832, 2.399432, 2.415648, 2.431848, 2.448032, 2.4642, 2.480352, 2.496488, 2.512608, 2.528712,
     2.5448, 2.560872, 2.576928, 2.592968, 2.608992, 2.625, 2.640992, 2.656968, 2.672928, 2.688872, 2.7048, 2.720712,
     2.736608, 2.752488, 2.768352, 2.7842, 2.800032, 2.815848, 2.831648, 2.847432, 2.8632, 2.878952, 2.894688, 2.910408,
     2.926112, 2.9418, 2.957472, 2.973128, 2.988768, 3.004392, 3.02, 3.035592, 3.051168, 3.066728, 3.082272, 3.0978,
     3.113312, 3.128808, 3.144288, 3.159752, 3.1752, 3.190632, 3.206048, 3.221448, 3.236832, 3.2522, 3.267552, 3.282888,
     3.298208, 3.313512, 3.3288, 3.344072, 3.359328, 3.374568, 3.389792, 3.405, 3.420192, 3.435368, 3.450528, 3.465672,
     3.4808, 3.495912, 3.511008, 3.526088, 3.541152, 3.5562, 3.571232, 3.586248, 3.601248, 3.616232, 3.6312, 3.646152,
     3.661088, 3.676008, 3.690912, 3.7058, 3.720672, 3.735528, 3.750368, 3.765192, 3.78, 3.794792, 3.809568, 3.824328,
     3.839072, 3.8538, 3.868512, 3.883208, 3.897888, 3.912552, 3.9272, 3.941832, 3.956448, 3.971048, 3.985632, 4.0002,
     4.014752, 4.029288, 4.043808, 4.058312, 4.0728, 4.087272, 4.101728, 4.116168, 4.130592, 4.145, 4.159392, 4.173768,
     4.188128, 4.202472, 4.2168, 4.231112, 4.245408, 4.259688, 4.273952, 4.2882, 4.302432, 4.316648, 4.330848, 4.345032,
     4.3592, 4.373352, 4.387488, 4.401608, 4.415712, 4.4298, 4.443872, 4.457928, 4.471968, 4.485992, 4.5, 4.513992,
     4.527968, 4.541928, 4.555872, 4.5698, 4.583712, 4.597608, 4.611488, 4.625352, 4.6392, 4.653032, 4.666848, 4.680648,
     4.694432, 4.7082, 4.721952, 4.735688, 4.749408, 4.763112, 4.7768, 4.790472, 4.804128, 4.817768, 4.831392, 4.845,
     4.858592, 4.872168, 4.885728, 4.899272, 4.9128, 4.926312, 4.939808, 4.953288, 4.966752, 4.9802, 4.993632, 5.007048,
     5.020448, 5.033832, 5.0472, 5.060552, 5.073888, 5.087208, 5.100512, 5.1138, 5.127072, 5.140328, 5.153568, 5.166792,
     5.18, 5.193192, 5.206368, 5.219528, 5.232672, 5.2458, 5.258912, 5.272008, 5.285088, 5.298152, 5.3112, 5.324232,
     5.337248, 5.350248, 5.363232, 5.3762, 5.389152, 5.402088, 5.415008, 5.427912, 5.4408, 5.453672, 5.466528, 5.479368,
     5.492192, 5.505, 5.517792, 5.530568, 5.543328, 5.556072, 5.5688, 5.581512, 5.594208, 5.606888, 5.619552, 5.6322,
     5.644832, 5.657448, 5.670048, 5.682632, 5.6952, 5.707752, 5.720288, 5.732808, 5.745312, 5.7578, 5.770272, 5.782728,
     5.795168, 5.807592, 5.82, 5.832392, 5.844768, 5.857128, 5.869472, 5.8818, 5.894112, 5.906408, 5.918688, 5.930952,
     5.9432, 5.955432, 5.967648, 5.979848, 5.992032, 6.0042, 6.016352, 6.028488, 6.040608, 6.052712, 6.0648, 6.076872,
     6.088928, 6.100968, 6.112992, 6.125, 6.136992, 6.148968, 6.160928, 6.172872, 6.1848, 6.196712, 6.208608, 6.220488,
     6.232352, 6.2442, 6.256032, 6.267848, 6.279648, 6.291432, 6.3032, 6.314952, 6.326688, 6.338408, 6.350112, 6.3618,
     6.373472, 6.385128, 6.396768, 6.408392, 6.42, 6.431592, 6.443168, 6.454728, 6.466272, 6.4778, 6.489312, 6.500808,
     6.512288, 6.523752, 6.5352, 6.546632, 6.558048, 6.569448, 6.580832, 6.5922, 6.603552, 6.614888, 6.626208, 6.637512,
     6.6488, 6.660072, 6.671328, 6.682568, 6.693792, 6.705, 6.716192, 6.727368, 6.738528, 6.749672, 6.7608, 6.771912,
     6.783008, 6.794088, 6.805152, 6.8162, 6.827232, 6.838248, 6.849248, 6.860232, 6.8712, 6.882152, 6.893088, 6.904008,
     6.914912, 6.9258, 6.936672, 6.947528, 6.958368, 6.969192, 6.98, 6.990792, 7.001568, 7.012328, 7.023072, 7.0338,
     7.044512, 7.055208, 7.065888, 7.076552, 7.0872, 7.097832, 7.108448, 7.119048, 7.129632, 7.1402, 7.150752, 7.161288,
     7.171808, 7.182312, 7.1928, 7.203272, 7.213728, 7.224168, 7.234592, 7.245, 7.255392, 7.265768, 7.276128, 7.286472,
     7.2968, 7.307112, 7.317408, 7.327688, 7.337952, 7.3482, 7.358432, 7.368648, 7.378848, 7.389032, 7.3992, 7.409352,
     7.419488, 7.429608, 7.439712, 7.4498, 7.459872, 7.469928, 7.479968, 7.489992, 7.5, 7.509992, 7.519968, 7.529928,
     7.539872, 7.5498, 7.559712, 7.569608, 7.579488, 7.589352, 7.5992, 7.609032, 7.618848, 7.628648, 7.638432, 7.6482,
     7.657952, 7.667688, 7.677408, 7.687112, 7.6968, 7.706472, 7.716128, 7.725768, 7.735392, 7.745, 7.754592, 7.764168,
     7.773728, 7.783272, 7.7928, 7.802312, 7.811808, 7.821288, 7.830752, 7.8402, 7.849632, 7.859048, 7.868448, 7.877832,
     7.8872, 7.896552, 7.905888, 7.915208, 7.924512, 7.9338, 7.943072, 7.952328, 7.961568, 7.970792, 7.98, 7.989192,
     7.998368, 8.007528, 8.016672, 8.0258, 8.034912, 8.044008, 8.053088, 8.062152, 8.0712, 8.080232, 8.089248, 8.098248,
     8.107232, 8.1162, 8.125152, 8.134088, 8.143008, 8.151912, 8.1608, 8.169672, 8.178528, 8.187368, 8.196192, 8.205,
     8.213792, 8.222568, 8.231328, 8.240072, 8.2488, 8.257512, 8.266208, 8.274888, 8.283552, 8.2922, 8.300832, 8.309448,
     8.318048, 8.326632, 8.3352, 8.343752, 8.352288, 8.360808, 8.369312, 8.3778, 8.386272, 8.394728, 8.403168, 8.411592,
     8.42, 8.428392, 8.436768, 8.445128, 8.453472, 8.4618, 8.470112, 8.478408, 8.486688, 8.494952, 8.5032, 8.511432,
     8.519648, 8.527848, 8.536032, 8.5442, 8.552352, 8.560488, 8.568608, 8.576712, 8.5848, 8.592872, 8.600928, 8.608968,
     8.616992, 8.625, 8.632992, 8.640968, 8.648928, 8.656872, 8.6648, 8.672712, 8.680608, 8.688488, 8.696352, 8.7042,
     8.712032, 8.719848, 8.727648, 8.735432, 8.7432, 8.750952, 8.758688, 8.766408, 8.774112, 8.7818, 8.789472, 8.797128,
     8.804768, 8.812392, 8.82, 8.827592, 8.835168, 8.842728, 8.850272, 8.8578, 8.865312, 8.872808, 8.880288, 8.887752,
     8.8952, 8.902632, 8.910048, 8.917448, 8.924832, 8.9322, 8.939552, 8.946888, 8.954208, 8.961512, 8.9688, 8.976072,
     8.983328, 8.990568, 8.997792, 9.005, 9.012192, 9.019368, 9.026528, 9.033672, 9.0408, 9.047912, 9.055008, 9.062088,
     9.069152, 9.0762, 9.083232, 9.090248, 9.097248, 9.104232, 9.1112, 9.118152, 9.125088, 9.132008, 9.138912, 9.1458,
     9.152672, 9.159528, 9.166368, 9.173192, 9.18, 9.186792, 9.193568, 9.200328, 9.207072, 9.2138, 9.220512, 9.227208,
     9.233888, 9.240552, 9.2472, 9.253832, 9.260448, 9.267048, 9.273632, 9.2802, 9.286752, 9.293288, 9.299808, 9.306312,
     9.3128, 9.319272, 9.325728, 9.332168, 9.338592, 9.345, 9.351392, 9.357768, 9.364128, 9.370472, 9.3768, 9.383112,
     9.389408, 9.395688, 9.401952, 9.4082, 9.414432, 9.420648, 9.426848, 9.433032, 9.4392, 9.445352, 9.451488, 9.457608,
     9.463712, 9.4698, 9.475872, 9.481928, 9.487968, 9.493992, 9.5, 9.505992, 9.511968, 9.517928, 9.523872, 9.5298,
     9.535712, 9.541608, 9.547488, 9.553352, 9.5592, 9.565032, 9.570848, 9.576648, 9.582432, 9.5882, 9.593952, 9.599688,
     9.605408, 9.611112, 9.6168, 9.622472, 9.628128, 9.633768, 9.639392, 9.645, 9.650592, 9.656168, 9.661728, 9.667272,
     9.6728, 9.678312, 9.683808, 9.689288, 9.694752, 9.7002, 9.705632, 9.711048, 9.716448, 9.721832, 9.7272, 9.732552,
     9.737888, 9.743208, 9.748512, 9.7538, 9.759072, 9.764328, 9.769568, 9.774792, 9.78, 9.785192, 9.790368, 9.795528,
     9.800672, 9.8058, 9.810912, 9.816008, 9.821088, 9.826152, 9.8312, 9.836232, 9.841248, 9.846248, 9.851232, 9.8562,
     9.861152, 9.866088, 9.871008, 9.875912, 9.8808, 9.885672, 9.890528, 9.895368, 9.900192, 9.905, 9.909792, 9.914568,
     9.919328, 9.924072, 9.9288, 9.933512, 9.938208, 9.942888, 9.947552, 9.9522, 9.956832, 9.961448, 9.966048, 9.970632,
     9.9752, 9.979752, 9.984288, 9.988808, 9.993312, 9.9978, 10.002272, 10.006728, 10.011168, 10.015592, 10.02,
     10.024392, 10.028768, 10.033128, 10.037472, 10.0418, 10.046112, 10.050408, 10.054688, 10.058952, 10.0632,
     10.067432, 10.071648, 10.075848, 10.080032, 10.0842, 10.088352, 10.092488, 10.096608, 10.100712, 10.1048,
     10.108872, 10.112928, 10.116968, 10.120992, 10.125, 10.128992, 10.132968, 10.136928, 10.140872, 10.1448, 10.148712,
     10.152608, 10.156488, 10.160352, 10.1642, 10.168032, 10.171848, 10.175648, 10.179432, 10.1832, 10.186952,
     10.190688, 10.194408, 10.198112, 10.2018, 10.205472, 10.209128, 10.212768, 10.216392, 10.22, 10.223592, 10.227168,
     10.230728, 10.234272, 10.2378, 10.241312, 10.244808, 10.248288, 10.251752, 10.2552, 10.258632, 10.262048,
     10.265448, 10.268832, 10.2722, 10.275552, 10.278888, 10.282208, 10.285512, 10.2888, 10.292072, 10.295328,
     10.298568, 10.301792, 10.305, 10.308192, 10.311368, 10.314528, 10.317672, 10.3208, 10.323912, 10.327008, 10.330088,
     10.333152, 10.3362, 10.339232, 10.342248, 10.345248, 10.348232, 10.3512, 10.354152, 10.357088, 10.360008,
     10.362912, 10.3658, 10.368672, 10.371528, 10.374368, 10.377192, 10.38, 10.382792, 10.385568, 10.388328, 10.391072,
     10.3938, 10.396512, 10.399208, 10.401888, 10.404552, 10.4072, 10.409832, 10.412448, 10.415048, 10.417632, 10.4202,
     10.422752, 10.425288, 10.427808, 10.430312, 10.4328, 10.435272, 10.437728, 10.440168, 10.442592, 10.445, 10.447392,
     10.449768, 10.452128, 10.454472, 10.4568, 10.459112, 10.461408, 10.463688, 10.465952, 10.4682, 10.470432,
     10.472648, 10.474848, 10.477032, 10.4792, 10.481352, 10.483488, 10.485608, 10.487712, 10.4898, 10.491872,
     10.493928, 10.495968, 10.497992, 10.5]

# MUDANÇAS NO RAIO DA BOLA E NO RAIO DO ROBÔ (DIVIDIMOS POR 2)
raio_bola = 0.00525
raio_robo = 0.002625
raio_intercep = raio_bola + raio_robo

x_robo = float(input("Digite a posicao X do robo: "))
y_robo = float(input("Digite a posicao Y do robo: "))

menor = 1000000000
indice_coordenada_x_próxima = 0
coordenada_mais_próxima = (0, 0)
a = 2.8
tempos_que_passarao = [] # ate a interceptação

# loop para encontrar a primeira coordenada na qual o robô consegue interceptar a bola dentro do tempo
for i in range(len(x)):
    x_bola = x[i]
    y_bola = y[i]
    t_bola = t[i]
    distancia = sqrt((x_robo - x_bola) ** 2 + (y_robo - y_bola) ** 2)
    dist_real = distancia + raio_intercep
    tempo_menor_dist = sqrt(dist_real / (0.5*a))
    tempos_que_passarao.append(t_bola)

    if tempo_menor_dist < t_bola: # se o robô chega a tempo de encontrar com a bola
        menor = distancia
        coordenada_x_próxima = x_bola
        coordenada_y_próxima = y_bola
        índice_da_coordenada_mais_próxima = i
        break

tempo_correspondente = t[índice_da_coordenada_mais_próxima]

print("\n1ª coordenada X da bola que o robo consegue interceptar:", coordenada_x_próxima)
print("\n1ª coordenada Y da bola que o robo consegue interceptar:", coordenada_y_próxima)
print("\nTempo em que a bola passara por esta coordenada: " + str(tempo_correspondente) + "s")
print("\nDistancia que o robo percorrera para alcançar a bola (entre o centro da bola e o centro do robo):", menor)
print("\nDistancia considerando o raio de interceptacao:", dist_real)
print("\nTempo que o robo demora para interceptar a bola:", tempo_menor_dist)
print("\nTempo que o robo espera pela bola:", tempo_correspondente - tempo_menor_dist)

# definição dos pontos da trajetória do robo:
posicoes_x_robo = []
posicoes_y_robo = []

ax = (x_bola - x_robo)/dist_real * a
lista_ax = []
ay = (y_bola - y_robo)/dist_real * a
lista_ay = []

cont = 0

while cont < len(tempos_que_passarao):
    x_agora = x_robo + (ax * (tempos_que_passarao[cont]**2))/2 # uso da fórmula da equação horária da posição para encontrar as posições do robo
    lista_ax.append(ax)
    y_agora = y_robo + (ay * (tempos_que_passarao[cont]**2))/2
    lista_ay.append(ay)
    posicoes_x_robo.append(x_agora)
    posicoes_y_robo.append(y_agora)
    cont += 1

# definição dos pontos da trajetória da bola:
posbolax = []
posbolay = []
cont2 = 0

while cont2 < len(tempos_que_passarao):
    posbolay.append(x[cont2])
    posbolax.append(y[cont2])
    cont2 += 1

# definição das velocidas vx e vy e ax e ay da bola e do robo 
vx_bola = []
vy_bola = []
vx_robo = []
vy_robo = []
cont3 = 0

vx_B = [(x[i+1] - x[i]) for i in range(len(x) - 1)]
vy_B = [(y[i+1] - y[i]) for i in range(len(y) - 1)]

t = 0.02

lista_ax_B = []
lista_ay_B = []

for i in range(len(tempos_que_passarao)):
    ax_B = (vx_B[i+1] - vx_B[i]) / t
    lista_ax_B.append(ax_B)
    ay_B = (vy_B[i+1] - vy_B[i]) / t
    lista_ay_B.append(ay_B)


while cont3 < len(tempos_que_passarao):
    # V = Vo + at
    vx_robo.append(ax * tempos_que_passarao[cont3])
    vy_robo.append(ay * tempos_que_passarao[cont3])

    vx_bola.append(ax_B * tempos_que_passarao[cont3])
    vy_bola.append(ay_B * tempos_que_passarao[cont3])
    cont3 += 1

distancias = []
cont4 = 0

while cont4 < len(tempos_que_passarao):
    x_B = x[cont4]
    y_B = y[cont4]
    x_R = posicoes_x_robo[cont4]
    y_R = posicoes_y_robo[cont4]

    dist = sqrt((x_R - x_B) ** 2 + (y_R - y_B) ** 2)
    distancias.append(dist)
    
    cont4 += 1

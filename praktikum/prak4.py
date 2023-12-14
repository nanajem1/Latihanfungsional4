import math

def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        x_baru = x + tx
        y_baru = y + ty
        return (x_baru, y_baru)
    return transformasi

def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        x_baru = x * sx
        y_baru = y * sy
        return (x_baru, y_baru)
    return transformasi

def rotasi(sudut):
    def transformasi(p):
        x, y = p
        sudut_radian = math.radians(sudut)
        x_baru = x * math.cos(sudut_radian) - y * math.sin(sudut_radian)
        y_baru = x * math.sin(sudut_radian) + y * math.cos(sudut_radian)
        return (x_baru, y_baru)
    return transformasi

def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    if p1[0] == p2[0]:
        return f"x = {p1[0]:.2f}"
    else:
        M = (p2[1] - p1[1]) / (p2[0] - p1[0])
        C = p1[1] - M * p1[0]
        return f"y = {M:.2f}x + {C:.2f}"

# Titik awal
titik_A = point(3, 4)
titik_B = point(5, 6)

# Persamaan garis awal
slope_awal = (titik_B[1] - titik_A[1]) / (titik_B[0] - titik_A[0])
intercept_awal = titik_A[1] - slope_awal * titik_A[0]

print(f'Persamaan garis yang melalui titik {titik_A} dan {titik_B}: \ny = {slope_awal:.2f}x + {intercept_awal:.2f}')

# Transformasi
titik_A_transformed, titik_B_transformed = dilatasi(1.5, 2)(rotasi(60)(translasi(2, -3)(titik_A))), dilatasi(1.5, 2)(rotasi(60)(translasi(2, -3)(titik_B)))


# Persamaan garis hasil transformasi
slope_transformed = (titik_B_transformed[1] - titik_A_transformed[1]) / (titik_B_transformed[0] - titik_A_transformed[0])
intercept_transformed = titik_A_transformed[1] - slope_transformed * titik_A_transformed[0]

print(f'Persamaan garis baru setelah transformasi: \ny = {slope_transformed:.2f}x + {intercept_transformed:.2f}')
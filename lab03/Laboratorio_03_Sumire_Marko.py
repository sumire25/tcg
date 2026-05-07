import math

def discrete_FT(signal):
  F = []
  n = len(signal)
  for u in range(n):
    Fu = complex(0, 0)
    for x in range(n):
      Fu += signal[x] * complex(math.cos(2 * math.pi * u * x / n), -math.sin(2 * math.pi * u * x / n))
    F.append(Fu)
  return F

def inv_discrete_FT(signal):
  f = []
  n = len(signal)
  for x in range(n):
    fx = complex(0, 0)
    for u in range(n):
      fx += signal[u] * complex(math.cos(2 * math.pi * u * x / n), math.sin(2 * math.pi * u * x / n))
    f.append(fx / n)
  return f
  
def round_signal(signal):
  for i in range(len(signal)):
    signal[i] = complex(round(signal[i].real, 3), round(signal[i].imag, 3))
  return signal

signal = [0, 0.707, 1 , 0.707, 0, -0.707, -1, -0.707]
ft_signal = discrete_FT(signal)
ft_signal = round_signal(ft_signal)
recovered_signal = inv_discrete_FT(ft_signal)
recovered_signal = round_signal(recovered_signal)
    
print("Original signal:")
print(signal)
print("Fourier Transform signal:")
print(ft_signal)
print("Recovered signal:")
print(recovered_signal)

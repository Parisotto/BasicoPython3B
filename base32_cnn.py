# pip install tensorflow
# pip install matplotlib

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Carrega o dataset MNIST (imagens 28x28 em tons de cinza)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normaliza os dados (0-255 → 0-1) e ajusta formato para CNN [samples, height, width, channels]
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# Define o modelo CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # 1º filtro
    layers.MaxPooling2D((2, 2)),                                            # Pooling
    layers.Conv2D(64, (3, 3), activation='relu'),                           # 2º filtro
    layers.MaxPooling2D((2, 2)),                                            # Pooling
    layers.Flatten(),                                                      # Achata tudo
    layers.Dense(64, activation='relu'),                                   # Camada densa
    layers.Dense(10, activation='softmax')                                 # Saída: 10 classes (0-9)
])

# Compila o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treina o modelo
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Avalia
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Acurácia no teste: {test_acc:.4f}")

# Acessa a primeira camada convolucional
first_conv_layer = model.layers[0]

# Obtém os pesos (filtros) da camada
filters, biases = first_conv_layer.get_weights()
print(f"Formato dos filtros: {filters.shape}")  # Ex: (3, 3, 1, 32) → 32 filtros de 3x3


# Normaliza para visualização
f_min, f_max = filters.min(), filters.max()
filters = (filters - f_min) / (f_max - f_min)

# Plota os 6 primeiros filtros da 1ª camada
n_filters = 6
plt.figure(figsize=(10, 4))
for i in range(n_filters):
    f = filters[:, :, 0, i]
    plt.subplot(1, n_filters, i+1)
    plt.imshow(f, cmap='gray')
    plt.axis('off')
    plt.title(f"Filtro {i+1}")
plt.suptitle("Filtros da 1ª camada convolucional")
plt.show()

# >>> AQUI: Visualização dos filtros da 2ª camada <<<

# Acessa a segunda camada convolucional
second_conv_layer = model.layers[2]

# Obtém os pesos (filtros) da camada
filters2, biases2 = second_conv_layer.get_weights()
print(f"Formato dos filtros (2ª camada): {filters2.shape}")  # (3, 3, 32, 64)

# Normaliza para visualização
f_min2, f_max2 = filters2.min(), filters2.max()
filters2 = (filters2 - f_min2) / (f_max2 - f_min2)

# Plota os 6 primeiros filtros da 2ª camada (canal 0)
plt.figure(figsize=(10, 4))
for i in range(n_filters):
    f = filters2[:, :, 0, i]  # visualizando apenas o canal 0
    plt.subplot(1, n_filters, i+1)
    plt.imshow(f, cmap='gray')
    plt.axis('off')
    plt.title(f"Filtro {i+1}")
plt.suptitle("Filtros da 2ª camada convolucional")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification


def log_loss(w, X, y):
    m = X.shape[0]

    z = X @ w  # линейная комбинация
    h = 1 / (1 + np.exp(-z))  # сигмоида

    loss = -np.mean(y * np.log(h + 1e-15) + (1 - y) * np.log(1 - h + 1e-15))
    grad = (1 / m) * X.T @ (h - y)
    return loss, grad

def optimize(w, X, y, n_iterations, eta):
    losses = []

    for i in range(n_iterations):
        loss, grad = log_loss(w, X, y)
        w = w - eta * grad
        losses.append(loss)

        # Выводим прогресс каждые 100 итераций
        if i % 100 == 0:
            print(f'Итерация {i}: Loss = {loss:.4f}')
    return w, losses


def predict(w, X, b=0.5):
    z = X @ w
    prob = 1 / (1 + np.exp(-z))

    y_predicted = (prob >= b).astype(int)
    return y_predicted, prob


def generate_data(n_samples = 100, n_features = 2):

    # Генерируем данные
    X, y = make_classification(
        n_samples = n_samples,
        n_features = n_features,
        n_informative = 2,
        n_redundant = 0,
        n_clusters_per_class = 1,
        flip_y = 0.1,
        random_state = 42
    )

    # Добавляем столбец единиц для смещения (bias term)
    X_bias = np.hstack([np.ones((X.shape[0], 1)), X])

    return X_bias, X, y


def run_experiment():
    # Генерируем данные
    n_samples = 200
    n_features = 2
    X_with_bias, X_original, y = generate_data(n_samples, n_features)

    # Инициализируем веса случайным образом
    np.random.seed(42)
    w_init = np.random.randn(X_with_bias.shape[1])

    # Параметры обучения
    n_iter = 500
    eta = 0.1  # скорость обучения

    print("Начинаем обучение: ")
    print(f"Количество итераций: {n_iter}")
    print(f"Скорость обучения (eta): {eta}")
    print(f"Размер данных: {X_with_bias.shape}")
    print("\n")

    # Обучаем модель
    w_trained, losses = optimize(w_init, X_with_bias, y, n_iter, eta)

    print("\n")
    print(f"Обучение завершено. Финальный loss: {losses[-1]:.4f}")

    # Делаем предсказания
    y_pred, prob = predict(w_trained, X_with_bias)

    # Вычисляем точность
    accuracy = np.mean(y_pred == y)
    print(f"Точность модели: {accuracy:.2%}")

    # 6. Визуализация результатов
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # График функции потерь
    axes[0].plot(losses)
    axes[0].set_title('Функция потерь во время обучения')
    axes[0].set_xlabel('Итерация')
    axes[0].set_ylabel('Loss')
    axes[0].grid(True)

    # Визуализация данных и разделяющей границы
    if n_features == 2:
        # Создаем сетку для разделяющей границы
        x1_min, x1_max = X_original[:, 0].min() - 0.5, X_original[:, 0].max() + 0.5
        x2_min, x2_max = X_original[:, 1].min() - 0.5, X_original[:, 1].max() + 0.5
        xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max, 100),
                               np.linspace(x2_min, x2_max, 100))

        # Предсказываем для точек сетки
        grid_with_bias = np.hstack([np.ones((xx1.ravel().shape[0], 1)),
                                    xx1.ravel().reshape(-1, 1),
                                    xx2.ravel().reshape(-1, 1)])
        Z, _ = predict(w_trained, grid_with_bias)
        Z = Z.reshape(xx1.shape)

        # Отображаем данные и границу решения
        axes[1].contourf(xx1, xx2, Z, alpha = 0.3, cmap = plt.cm.RdYlBu)
        axes[1].scatter(X_original[y == 0, 0], X_original[y == 0, 1],
                        c='blue', label='Класс 0', alpha=0.6)
        axes[1].scatter(X_original[y == 1, 0], X_original[y == 1, 1],
                        c='red', label='Класс 1', alpha=0.6)
        axes[1].set_title('Разделяющая граница и данные')
        axes[1].set_xlabel('Признак 1')
        axes[1].set_ylabel('Признак 2')
        axes[1].legend()
        axes[1].grid(True)

    # Матрица ошибок
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y, y_pred)

    im = axes[2].imshow(cm, interpolation='nearest', cmap = plt.cm.Blues)
    axes[2].set_title('Матрица ошибок')
    axes[2].set_xlabel('Предсказанный класс')
    axes[2].set_ylabel('Истинный класс')
    axes[2].set_xticks([0, 1])
    axes[2].set_yticks([0, 1])

    # Добавляем текст в ячейки матрицы
    for i in range(2):
        for j in range(2):
            axes[2].text(j, i, str(cm[i, j]),
                         ha="center", va="center",
                         color="white" if cm[i, j] > cm.max() / 2 else "black")

    plt.tight_layout()
    plt.show()

    return w_trained, losses, accuracy

w_trained, losses, accuracy = run_experiment()
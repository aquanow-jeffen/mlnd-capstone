import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def inceptLoss():
    df = pd.read_csv('saved_models/incept_hist.csv')

    fig, ax = plt.subplots()
    ax.plot(df.index, df['loss'], label="loss")
    ax.plot(df.index, df['val_loss'], label="val_loss")
    ax.legend()
    ax.set_title('InceptionV3')
    ax.set_xlabel('epoch')

    plt.show()

def mobileNetLoss():
    df = pd.read_csv('saved_models/hist_mbnet.csv')

    fig, ax = plt.subplots()
    ax.plot(df.index, df['loss'], label="loss")
    ax.plot(df.index, df['val_loss'], label="val_loss")
    ax.legend()
    ax.set_title('MobileNetV2')
    ax.set_xlabel('epoch')

    plt.show()

def inceptConfusion(model, test_tensors, test_targets):
    predictions = [np.argmax(model.predict(np.expand_dims(tensor, axis=0))) for tensor in test_tensors]
    y_pred = np.array(predictions)
    y_test = np.argmax(test_targets, axis=1)
    cnf_matrix = confusion_matrix(y_test, y_pred)
    np.set_printoptions(precision=2)

    class_names = range(0,99)
    # Plot normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')
    plt.show()
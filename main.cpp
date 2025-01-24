
#include "final_cross_compiler.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    final_cross_compiler w;
    w.show();
    return a.exec();
}

#include "final_cross_compiler.h"
#include <pybind11/pybind11.h>
#include<pybind11/numpy.h>
#include <pybind11/embed.h>
#include <iostream>
#include <vector>
namespace py = pybind11;
final_cross_compiler::final_cross_compiler(QWidget *parent)
    : QMainWindow(parent)
{
    ui.setupUi(this);
    connect(ui.pushButton, SIGNAL(clicked()), this, SLOT(showInformationMessageBox()));
}



void final_cross_compiler::showInformationMessageBox() {
    py::object result1;
    //py::str py_str;

    py::scoped_interpreter guard{};


    py::eval_file("script.py");
    py::object  caller = py::module::import("__main__").attr("caller");
    f1 = ui.lineEdit->text()  ;
    f2 =  ui.lineEdit_2->text();
    qint32 threshold=ui.Threshold->value();

    if (ui.lineEdit->text() == "")
    {
        f1= "YOUR PATH\\PCL3 - Cloud.ply";
        f2= "YOUR PATH\\PCL1 - Cloud.ply";
    }
    
    QByteArray byteArray1 = f1.toUtf8();
    std::string  stdstr1(byteArray1.constData(), byteArray1.size());
    QByteArray byteArray2 =  f2.toUtf8();
    std::string   stdstr2 (byteArray2.constData(), byteArray2.size());

    int check=0;
    if (ui.checkBox->isChecked()) {
        check = 1;
    }


    QString text = ui.lineEdit_3->text(); // Get the text from the QLineEdit
    std::string utf8_text = text.toUtf8().constData();
    
    
  
    result1 = caller(stdstr1, stdstr2, threshold, check,utf8_text);
    s = result1.cast<std::string>();
    strss = QString::fromStdString(s);
    ui.label->setText(strss);



}


final_cross_compiler::~final_cross_compiler()
{}

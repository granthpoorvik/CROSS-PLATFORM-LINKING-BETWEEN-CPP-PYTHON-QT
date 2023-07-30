#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_final_cross_compiler.h"

class final_cross_compiler : public QMainWindow
{
    Q_OBJECT

public:
    final_cross_compiler(QWidget *parent = nullptr);
    ~final_cross_compiler();
    std::string s ;
    std::string s1;
    std::string s2;
    
    
    QString strss = '\0';
    QString f1, f2 = '\0';
    //pybind11::str py_str;
   
private:
    Ui::final_cross_compilerClass ui;
public  slots:

    //void showInformationMessageBox(std::string);
    void showInformationMessageBox();

    //std::string runPythonScriptAndGetOutput(const std::string);
};

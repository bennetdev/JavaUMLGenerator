from writer import Writer

Writer({
    "Class1": {
        "variables": ["var1", "var2"],
        "methods": ["method1", "method2"]
    },
    "Class2": {
        "variables": ["var3", "var4"],
        "methods": ["method3", "method4"]
    }
},
).write_to_pdf()

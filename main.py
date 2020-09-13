from writer import Writer

Writer({
    "Class1": {
        "variables": ["var1", "var2"],
        "methods": ["method1", "method2"]
    },
    "Class2": {
        "variables": ["var3", "var4"],
        "methods": ["method3", "method4"]
    },
    "Class3": {
        "variables": ["var5", "var6"],
        "methods": ["method5", "method6"]
    },
    "Class4": {
        "variables": ["var5", "var6"],
        "methods": ["method5", "method6"]
    },
    "Class5": {
        "variables": ["var5", "var6"],
        "methods": ["method5", "method6"]
    },
    "Class6": {
        "variables": ["var5", "var6"],
        "methods": ["method5", "method6"]
    }
},
).write_to_pdf()

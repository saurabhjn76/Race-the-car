import cx_Freeze

executables=[cx_Freeze.Executable("Race_the_car.py")]
cx_Freeze.setup(

	name="RacetheCar",
	options={"build_exe":{"packages":["pygame","sys","pygame.surfarray","numpy","pygame._numpysurfarray"],
						  "include_files": ["red2.jpg","blue2.jpg","car_11.png","car_22.png"]}},
						 
	executables=executables		
	)
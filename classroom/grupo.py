from classroom.asignatura import Asignatura

class Grupo:
    grado = None


    def __init__(self, grupo="grupo predeterminado", asignaturas=None,estudiantes=None):
        if estudiantes == None:
            estudiantes = []
        
        if asignaturas == None:
            asignaturas = []
        
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.asignarNombre("Grado 12")
        
    
    def __str__(self):
        return "Grupo de estudiantes: "+self._grupo

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista


    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 10"):
    #     cls.grado = nombre


    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre
    
    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 12"):
    #     cls.grado = nombre
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

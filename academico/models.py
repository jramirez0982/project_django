from django.db import models

# Create your models here.

#crearemos una tabla CARRERA
class Carrera(models.Model) :
    id = models.BigAutoField(verbose_name = "CÓDIGO", primary_key=True) # creo la primary key de la tabla con un campo autoincremental, se proyecta con el nombre de codigo
    carrera = models.CharField(verbose_name="CARRERA", max_length=30) #creo el campo carrera de maximo 30 caracteres
    facultad = models.CharField(verbose_name="FACULTAD",max_length=30) # creo el campo Facultad

# CREAR TABLA MATERIAS
class Materia(models.Model) :
    id = models.BigAutoField(verbose_name = "CÓDIGO", primary_key=True) # creo la primary key de la tabla con un campo autoincremental, 
    materia = models.CharField(verbose_name="MATERIA", max_length=30) #creo el campo carrera de maximo 30 caracteres
    creditos = models.PositiveIntegerField(verbose_name="CREDITOS")
    descripcion = models.CharField(verbose_name = "DESCRIPCION", max_length = 100, blank=True, null=True)
    jornadas = [("M", "MAÑANA"), ("N", "NOCHE"), ("FDS", "FIN DE SEMANA")]
    jornada = models.CharField(verbose_name = "JORNADA", max_length = 3, choices = jornadas)

# MALLA CURRICULAR
class Malla(models.Model)  :
    id = models.BigAutoField(verbose_name = "CÓDIGO", primary_key=True) # creo la primary key de la tabla con un campo autoincremental, 
    carrera = models.ForeignKey(Carrera, on_delete = models.CASCADE) #creo el campo carrera de maximo 30 caracteres
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE) #creo el campo carrera de maximo 30 caracteres

# DOCENTES

class Docente(models.Model) :
    id = models.BigAutoField(verbose_name = "CÓDIGO", primary_key=True) # creo la primary key de la tabla con un campo autoincremental, 
    nombre = models.CharField(verbose_name = "NOMBRE", max_length=25) #creo el campo carrera de maximo 30 caracteres
    apellido = models.CharField(verbose_name = "APELLIDO", max_length=25)
    email = models.EmailField(verbose_name = "CORREO", max_length=50, unique=True)
    nacimiento = models.DateField(verbose_name = "FECHA DE NACIMIENTO")
    telefono = models.PositiveBigIntegerField(unique=True)
    #INSTALAR DBeaver choices en models

#ASIGNACION ACADEMICA - ID -DOCENTES - MATERIAS - PERIODO

class AsignacionAcademica(models.Model) :
    id = models.BigAutoField(verbose_name = "CÓDIGO", primary_key=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, blank = True, null = True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodo = models.CharField(verbose_name="PERIODO ACADEMICO", max_length=7)

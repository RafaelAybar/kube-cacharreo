## Configuraciones de Google Kubernetes Engine

### Securización de la infraestructura

### 1.  Permisos de Google Cloud mínimos y roles recomendados
    * Cuentas de servicio
    * Gestión de usuarios

### 2.  Mantenimiento


#### Configuración del mantenimiento automático

En GKE, al crear un clúster tenemos la oportunidad de habilitar una opción llamada mantenimiento automático. Esta opción
permite que Google aplique parches automáticamente. Para que no haya pérdida de servicio se requieren 3 nodos.

No obstante, debemos de configurar **cuándo** se harán efectivos estos parches (día de la semana y hora), así como establecer
un rango de tiempo en el que no se aplicará ninguna actualización, por ejemplo, del 25 de Diciembre al 4 de Enero.

En el menú de creación del clúster hay un apartado llamado ventana de mantenimiento, ahí clicamos en el **Hora de inicio** y
cambiamos el valor En cualquier momento por la hora que mejor nos convenga.

![horario](imagenes/horario.png)
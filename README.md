Partición de equivalencias 

nombre Partición | rango | valor prueba | resultado 
Dentro gratuito  | <=30 | 15 min | 0-> valido 
Limite exacto | = 30 | 30 | 0 -> valido
Fuera gratuito |<30 | 31 min | 500 -> valido
Negativo | > 0 | -5 min | error 


VALORES LIMITE

Límite Analizado | Valor de Prueba | Posición respecto al Límite | Estado del Rango | Resultado Esperado

Borde inferior (0.0) | -1 | Justo antes | Fuera | Falla: Error de validación
Borde inferior (0.0|) | 0.0 | Exacto | Dentro | Exitoso: cobro 0
Borde inferior (0.0) | 1 | Justo déspues | Dentro | Exitoso: cobro 0 

Aprobación borde inferior (30) | 29| Justo antes | Dentro | Exitoso: cobro 0
Aprobación borde inferior (30|) | 30 | Exacto | Dentro | Exitoso: cobro 0
Aprobación borde inferior (30) | 31 | Justo déspues | Dentro | Exitoso: cobro 500

Borde superior (1440) | 1439 | Justo antes | Dentro | Exitoso: 11750
Borde superior (1440|) | 1440 | Exacto | Dentro | Exitoso: cobro 12000
Borde superior (1440) | 1441 | Justo déspues | Fuera | Exitoso: cobro 12000
from django.urls import path
from AppBcs.views import*

urlpatterns=[   
 
    path ('', inicio,name="inicio"),
    path('consolas/', ConsolaListView.as_view(), name='ListarConsolas'),
    path('consolas/crear/', ConsolaCreateView.as_view(), name='CrearConsola'),
    path('consolas/<int:pk>/actualizar/', ConsolaUpdateView.as_view(), name='ActualizarConsola'),
    path('consolas/<int:pk>/borrar/', ConsolaDeleteView.as_view(), name='BorrarConsola'),

    path('perifericos/', PerifericoListView.as_view(), name='ListarPerifericos'),
    path('perifericos/crear/', PerifericoCreateView.as_view(), name='CrearPeriferico'),
    path('perifericos/<int:pk>/actualizar/', PerifericoUpdateView.as_view(), name='ActualizarPeriferico'),
    path('perifericos/<int:pk>/borrar/', PerifericoDeleteView.as_view(), name='BorrarPeriferico'),

    path('juegos/', JuegoListView.as_view(), name='ListarJuegos'),
    path('juegos/crear/', JuegoCreateView.as_view(), name='CrearJuego'),
    path('juegos/<int:pk>/actualizar/', JuegoUpdateView.as_view(), name='ActualizarJuego'),
    path('juegos/<int:pk>/borrar/', JuegoDeleteView.as_view(), name='BorrarJuego'),

    path('funkos/', FunkoListView.as_view(), name='ListarFunkos'),
    path('funkos/crear/', FunkoCreateView.as_view(), name='CrearFunko'),
    path('funkos/<int:pk>/actualizar/', FunkoUpdateView.as_view(), name='ActualizarFunko'),
    path('funkos/<int:pk>/borrar/', FunkoDeleteView.as_view(), name='BorrarFunko'),
    path('presentacion/',presentacion,name="presentacion"),
    
    
]


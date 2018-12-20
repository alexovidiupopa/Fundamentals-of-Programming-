from repo.repoRoutes import RoutesRepository
from repo.repoBuses import BusesRepository
from controller.controller import AppController
from ui.ui import Console


repoRoutes = RoutesRepository("routes.txt")
repoBuses = BusesRepository("buses.txt")

controller = AppController(repoRoutes,repoBuses)

console = Console(controller)
console.run()
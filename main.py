from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.align import Align
import time
import sys
from polyz_functions import (
    get_market_details_by_slug,
    market_analyzer,
    market_insight_dashboard,
    price_evolution_with_fill,
    trade_analytics,
    plot_gradient_scatter_analytics,
    plot_advanced_gradient_scatter,
    plot_outcome_gradient_analytics,
    plot_advanced_distribution_gradients,
    plot_trader_strategy_analysis,
    plot_trader_timing_analysis,
)

console = Console()


def market_analysis(market_slug):
    console.print()
    console.print(Panel.fit(
        f"[bold cyan]🔍 Analyzing Market[/bold cyan]\n[dim]{market_slug}[/dim]",
        border_style="cyan",
        box=box.DOUBLE
    ))
    console.print()

    with Progress(
        SpinnerColumn(spinner_name="dots"),
        TextColumn("[cyan]{task.description}"),
        BarColumn(complete_style="cyan", finished_style="green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:

        task1 = progress.add_task("📊 Fetching market details...", total=100)
        market = get_market_details_by_slug(market_slug)
        progress.update(task1, completed=100)

        task2 = progress.add_task("📈 Running market analyzer...", total=100)
        market_analyzer(market_slug)
        progress.update(task2, completed=100)

        task3 = progress.add_task(
            "🎯 Generating insight dashboard...", total=100)
        market_insight_dashboard(market_slug)
        progress.update(task3, completed=100)

        task4 = progress.add_task(
            "📊 Creating gradient scatter analytics...", total=100)
        plot_gradient_scatter_analytics(market_slug)
        progress.update(task4, completed=100)

        task5 = progress.add_task(
            "🎨 Generating advanced scatter plots...", total=100)
        plot_advanced_gradient_scatter(market_slug)
        progress.update(task5, completed=100)

    console.print()
    console.print(Panel(
        f"[bold green]✅ Success![/bold green]\n\n"
        f"[cyan]Plots for market[/cyan] [bold yellow]\"{market_slug}\"[/bold yellow] [cyan]have been generated and saved in the directory.[/cyan]\n\n"
        f"[dim]📁 Output: ./analyzer-outputs/{market_slug}/[/dim]",
        title="[bold white]📊 Market Analysis Complete[/bold white]",
        border_style="green",
        box=box.ROUNDED
    ))








=========================================================================================================

Pay & get full source code here: 

https://pay.oxapay.com/17944852



=========================================================================================================


  

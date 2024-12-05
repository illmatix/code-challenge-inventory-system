import os
import importlib
import click

def register_seed_command(app):
    """
    Registers the 'seed' command to the Flask CLI.
    """

    @app.cli.command("seed")
    @click.argument("seeders", nargs=-1)  # Allow multiple arguments for specific seeders
    def seed_command(seeders):
        """
        Runs specific or all seeders in the seeders directory.

        Usage:
        - Run all seeders: flask seed
        - Run specific seeders: flask seed admin_seeder product_seeder
        """
        seeders_path = os.path.join(os.path.dirname(__file__), "..", "seeders")
        print(f"Running seeders from directory: {seeders_path}")

        if not seeders:
            # If no specific seeders are provided, run all seeders
            print("No specific seeders provided. Running all seeders.")
            for filename in os.listdir(seeders_path):
                if filename.endswith(".py") and not filename.startswith("__"):
                    run_seeder(filename, seeders_path)
        else:
            # Run only the specified seeders
            for seeder_name in seeders:
                filename = f"{seeder_name}.py"
                if filename in os.listdir(seeders_path):
                    run_seeder(filename, seeders_path)
                else:
                    print(f"Seeder '{seeder_name}' not found.")

        print("Seeders execution completed.")

    def run_seeder(filename, seeders_path):
        """Dynamically import and run a specific seeder."""
        module_name = f"app.seeders.{filename[:-3]}"  # Remove `.py` extension
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "run"):
                print(f"Running seeder: {module_name}")
                module.run()
            else:
                print(f"Skipping {module_name}: No 'run()' function found.")
        except Exception as e:
            print(f"Error running seeder {module_name}: {e}")

from workflows.execution_flow import run_workflow


def main():
    print("=" * 50)
    print("   Multi-Agent AI Research Assistant")
    print("=" * 50)

    user_query = input("\nEnter your task: ").strip()

    if not user_query:
        print("No input provided. Exiting.")
        return

    final_answer = run_workflow(user_query)

    print("\n" + "=" * 50)
    print("FINAL OUTPUT")
    print("=" * 50)
    print(final_answer)


if __name__ == "__main__":
    main()

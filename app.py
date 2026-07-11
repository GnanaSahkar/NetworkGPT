from services.ai.ai_service import AIService


def main():
    ai = AIService()

    print("=" * 80)
    print("GENERAL QUESTION")
    print("=" * 80)
    print(ai.ask("What is OSPF?"))

    print("\n" + "=" * 80)
    print("COMMAND EXPLANATION")
    print("=" * 80)
    print(ai.explain_command("aaa new-model"))

    sample_config = """
hostname R1
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
"""

    print("\n" + "=" * 80)
    print("CONFIGURATION SUMMARY")
    print("=" * 80)
    print(ai.summarize_configuration(sample_config))


if __name__ == "__main__":
    main()
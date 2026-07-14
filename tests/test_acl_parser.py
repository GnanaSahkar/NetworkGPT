
from services.parser.parsers.acl_parser import ACLParser
from utils.logger import logger

def main():
    logger.info("ACL parser intialized") 
    config = """
ip access-list extended INTERNET-IN

 permit tcp any any eq 80

 permit tcp any any eq 443

 deny ip any any
    """
    parser = ACLParser()
    acl = parser.parse(config)
    logger.success("ACL congig parsed sucesfully.")
    print("\n")
    print("=" * 80)
    print("ACL PARSER")
    print("=" * 80)
    
    print(acl)
    
if __name__ == "__main__":
    main()
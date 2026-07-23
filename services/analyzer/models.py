from dataclasses import dataclass, field

@dataclass
class Finding:
    """
        Represent a single analysis finding.
        """
    
    category: str
    severity: str
    title: str
    description: str
    recommendation: str
    
@dataclass
class AnalysisReport:
    """ Represents the complete analysis report.
    """
    
    findings: list[Finding] = field(default_factory=list)
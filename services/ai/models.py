"""
Models used by the AI framework.
"""

from dataclasses import dataclass


@dataclass
class AIReport:
    """
    Represents the AI-generated report for a network configuration analysis.
    """

    executive_summary: str
    technical_summary: str
    risk_assessment: str
    recommendations: str
    remediation_plan: str
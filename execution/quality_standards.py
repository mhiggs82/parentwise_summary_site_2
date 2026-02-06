import sys

# ParentWise Actionable Insight Guides - Quality Standards Manifesto

QUALITY_MANIFESTO = """
# PARENTWISE QUALITY STANDARDS FOR SEMANTIC EXTRACTION

## 1. THE "WHY IT MATTERS" (EXECUTIVE SUMMARY)
- MODEL: Must follow the [Thesis] -> [Unique Contribution] -> [Target Outcome] flow.
- ROBUSTNESS: Exactly 3 to 4 sentences about the book's main thesis. No more, no less.
- IMPACT: Concisely capture the central philosophical shift or tactical breakthrough.
- TONE: Compelling, authoritative, yet empathetic.

## 2. ANALYSIS & INSIGHTS (THE LEARNING TAB)
- FIDELITY: Preserve the author's specific terminology and logic.
- SCHEMA:
  * 'heading': Clear, thematic title.
  * 'intro_text': 2-3 sentences of deep semantic context.
  * 'insight_card': MUST be an object { "title": "...", "icon": "...", "text": "..." }.
- INSIGHT CARDS: The 'text' within must be a standalone "nugget" of wisdom.

## 3. ACTIONABLE FRAMEWORK (THE DOING TAB)
- QUANTITY: Provide exactly 3 to 5 action frameworks per book. No more, no less.
- STRUCTURE: Each framework MUST contain between 3 to 7 actionable steps.
- CONTEXT: Each process must have a 'context' field explaining *when* or *why* to use it.
- STEPS SCHEMA: Every step must have 'bold_title' and 'description'.
- BOLD TITLES: Use high-energy imperative phrases. NEVER use a single word (e.g., ❌ NO: "PAUSE", "OBSERVE"; ✅ YES: "PAUSE and breathe", "OBSERVE physiological cues"). The title must complete a thought and start with a verb.
- DESCRIPTIONS: Start with verb but ALWAYS include a complete, strong descriptive sentence, not just a fragment. Example ❌ WRONG: bold_title: "Approach", description: "within comfortable physical proximity before speaking". Example ✅ RIGHT: bold_title: "Match the tone", description: "Lower to eye level and use a soothing voice to meet their right-brain state." The description should be a full sentence explaining HOW and WHY, with clear actionable detail.
- SECTION HEADERS: Do NOT mix section headers (e.g., "STEP ONE", "STEP TWO") with numbered steps (e.g., "1.", "2."). Instead, use consistent action-oriented bold_titles without numbers. Example ❌ WRONG: bold_title: "STEP", description: "ONE: Address the Threat" followed by bold_title: "1.", description: "Identify...". Example ✅ RIGHT: bold_title: "IDENTIFY potential threats", description: "sensory, environmental, social, or internal cues..."
- SUCCESS CHECKS: The final step of a process should include a **Success Check** or **Warning** caveat.

## 4. METADATA & HERO
- SUBTITLE: Should summarize the book's core premise in one power-sentence.
- TAGS: Minimum 4 tags reflecting both theme (e.g., Attachment) and application (e.g., Tantrums).
- HERO COUNTS: 'insights_count' and 'actions_count' must exactly match the number of items in the tabs.
- BADGE: Must be '[CATEGORY] Core Read'.

## 5. TECHNICAL CONSTRAINTS
- JSON ONLY: Return nothing but the valid JSON object.
- NO ESCAPING ERRORS: Ensure backslashes and quotes are properly escaped to prevent YAML errors in MDX.
"""

def print_standards():
    """Prints the quality standards for the LLM context."""
    print(QUALITY_MANIFESTO)

if __name__ == "__main__":
    print_standards()

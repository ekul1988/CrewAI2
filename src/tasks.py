from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(
                f"""
                Conduct comprehensive researcg on each of the individuals and companies involved in the upcoming meeting. Gather information on recent news, achievements, professional background, and any relevant business activities.
                
                Participants: {meeting_participants}
                Meeting Context: {meeting_context}
                """
            ),
            expected_output=dedent(f"""\A detailed report summarizing key kindings about each participant and company, highlighting information that could be relevant for the meeting."""), 
            agent=agent,
            async_execution=True, 
            )
    def industry_analysis_task(self, agent, participants, meeting_context):
        return Task(
            description=dedent(f"""\
            Analyze the current industry trends, challenges, and opportunitties relavent to the meetins's context. Consider market reports, recent developments, and expert opinions to provide a comprehensive overview of the industry landscape. 
            Participants: {participants}
            Meeting Context: {meeting_context}"""),
        expected_output=dedent(f"""\
                An insightful analysis that identifies major trends, potentail chatllenges and opportunities"""),
        async_execution=True,
        agent=agent,
        )
    def meeting_strategy_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description=dedent(f"""\
                Develop strategic talking points, questions, and discussion angles for the meeting based on the research and industry analysis conducted. 
                Meeting Context: {meeting_context}
                Meeting Objective: {meeting_objective}"""),
            expected_output=dedent(f"""\Complete report with a list of key talking points, strategic questions to ask to help achieve the meeting's objective during the meeting"""),
            agent=agent)
    def summary_and_briefing_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description=dedent(f"""\
                Compile research findins, industry analysis, and strategic talking points into a concise, comprehensive briefing document for the meeting. Ensure the breifing is easy to digest and equips the meeting particapants with the necessary information and strategies.
                Meeting Context: {meeting_context}
                Meeting Objective: {meeting_objective}"""),
            expected_output=dedent(f"""\A well-structured breifing document that includes sections for participant bios, industry overview,  talking points, and strategic recomendations."""),
            agent=agent
        )
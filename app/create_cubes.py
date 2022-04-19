import atoti as tt

from .constants import (
    Cube,
    ElectionCubeLevel,
    ElectionCubeMeasure,
    ElectionCubeHierarchy,
    LocationTableColumn,
    StateResultsTableColumn,
    StatisticsTableColumn,
    Table,
)


def create_election_cube(session: tt.Session, /) -> None:
    candidate_table = session.tables[Table.CANDIDATE_TBL.value]
    # candidate_dtl_table = session.tables[Table.CANDIDATE_DTL_TBL]
    state_results_table = session.tables[Table.STATE_RESULTS_TBL.value]
    statistics_table = session.tables[Table.STATISTICS_TBL.value]
    location_table = session.tables[Table.LOCATION_TBL.value]

    cube = session.create_cube(candidate_table, Cube.ELECTION_CUBE.value)
    h, l, m = cube.hierarchies, cube.levels, cube.measures

    h[ElectionCubeHierarchy.RESULT_DATE.value].slicing = True
    l[ElectionCubeLevel.RESULT_DATE.value].order = tt.NaturalOrder(ascending=False)

    # define measures for statistics table
    m_name_stats = [
        ele
        for ele in statistics_table.columns
        if ele
        not in [
            StatisticsTableColumn.RESULT_DATE.value,
            StatisticsTableColumn.DEPARTMENT.value,
            StatisticsTableColumn.REGION.value,
        ]
    ]
    print("================", m_name_stats)

    for m_name in m_name_stats:
        print("--------- MEASURE NAMES:", m_name)
        m[m_name] = tt.value(
            statistics_table[m_name],
            levels=[
                l[ElectionCubeLevel.DEPARTMENT.value],
                l[ElectionCubeLevel.REGION.value],
            ],
        )

        # to sum up the statistics from Department/Region and above
        m[f"Total {m_name}".capitalize()] = tt.agg.sum(m[m_name])

    m.update(
        {
            ElectionCubeMeasure.NUM_DEPARTMENTS.value: tt.agg.count_distinct(
                state_results_table[StateResultsTableColumn.DEPARTMENT.value]
            ),
            ElectionCubeMeasure.NUM_REGIONS.value: tt.agg.count_distinct(
                state_results_table[StateResultsTableColumn.REGION.value]
            ),
            ElectionCubeMeasure.LONGITUDE.value: tt.value(
                location_table[LocationTableColumn.LONGITUDE.value]
            ),
            ElectionCubeMeasure.LATITUDE.value: tt.value(
                location_table[LocationTableColumn.LATITUDE.value]
            ),
            ElectionCubeMeasure.VOTES.value: tt.value(
                state_results_table[StateResultsTableColumn.VOTES.value],
                levels=[
                    l[StateResultsTableColumn.RESULT_DATE.value],
                    l[StateResultsTableColumn.REGION.value],
                    l[StateResultsTableColumn.DEPARTMENT.value],
                    l[StateResultsTableColumn.CANDIDATE_NAME.value],
                ],
            ),
        }
    )

    m.update(
        {
            ElectionCubeMeasure.TOTAL_VOTES_DEPARTMENTS.value: tt.agg.sum(
                m[ElectionCubeMeasure.VOTES.value],
                scope=tt.scope.origin(l[ElectionCubeLevel.CANDIDATE_NAME.value]),
            ),
            # ElectionCubeMeasure.PERCENT_REG_VOTES.value: m[
            #     ElectionCubeMeasure.TOTAL_VOTES_DEPARTMENTS.value
            # ]
            # / m[ElectionCubeMeasure.TOTAL_REG_VOTERS.value],
            # ElectionCubeMeasure.PERCENT_VALID_VOTES.value: m[
            #     ElectionCubeMeasure.TOTAL_VALID_VOTES.value
            # ]
            # / m[ElectionCubeMeasure.TOTAL_REG_VOTERS.value],
            # ElectionCubeMeasure.PERCENT_BLANK_VOTES.value: m[
            #     ElectionCubeMeasure.TOTAL_BLANK_VOTES.value
            # ]
            # / m[ElectionCubeMeasure.TOTAL_REG_VOTERS.value],
            # ElectionCubeMeasure.PERCENT_NULL_VOTES.value: m[
            #     ElectionCubeMeasure.TOTAL_NULL_VOTES.value
            # ]
            # / m[ElectionCubeMeasure.TOTAL_REG_VOTERS.value],
            # ElectionCubeMeasure.PERCENT_ABSTENTIONS.value: m[
            #     ElectionCubeMeasure.TOTAL_ABSTENTIONS.value
            # ]
            # / m[ElectionCubeMeasure.TOTAL_REG_VOTERS.value],
            # ElectionCubeMeasure.TOTAL_INVALID_VOTES.value: m[
            #     ElectionCubeMeasure.TOTAL_BLANK_VOTES.value
            # ]
            # + m[ElectionCubeMeasure.TOTAL_NULL_VOTES.value]
            # + m[ElectionCubeMeasure.TOTAL_ABSTENTIONS.value],
            # ElectionCubeMeasure.PERCENT_INVALID.value: m[
            #     ElectionCubeMeasure.TOTAL_INVALID_VOTES.value
            # ]
            # / m[ElectionCubeMeasure.TOTAL_REG_VOTERS.value],
            # ElectionCubeMeasure.WINNING_CANDIDATE.value: tt.agg.max_member(
            #     m[ElectionCubeMeasure.TOTAL_VOTES_DEPARTMENTS.value],
            #     l[ElectionCubeLevel.CANDIDATE_NAME.value],
            # ),
            # ElectionCubeMeasure.WINNING_VOTES.value: tt.agg.max(
            #     m[ElectionCubeMeasure.TOTAL_VOTES_DEPARTMENTS.value],
            #     scope=tt.scope.origin(l[ElectionCubeLevel.CANDIDATE_NAME.value]),
            # ),
        }
    )

    for measure_name in m.keys():
        if "% " in measure_name:
            m[measure_name].formatter = "DOUBLE[0.000%]"


def create_cubes(session: tt.Session, /) -> None:
    create_election_cube(session)

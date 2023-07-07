# generated by datamodel-codegen:
#   filename:  bench.yaml
#   timestamp: 2023-06-21T19:01:59+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from arthur_bench.models.client import Page, PageSize, TotalCount, TotalPages
from pydantic import BaseModel, Field

class ScoringMethod(str, Enum):
    BERTScore = 'bertscore'
    SummaryQuality = 'summary_quality'
    QACorrectness = 'qa_correctness'

class TestCaseRequest(BaseModel):
    """
    An input, reference output pair.
    """

    input: str
    """
    Input to the test case. Does not include the prompt template.
    """
    reference_output: Optional[str]
    """
    Reference or "Golden" output for the given input.
    """


class TestSuiteRequest(BaseModel):
    """
    Test case data and metadata for the test suite.
    """
    name: str
    description: Optional[str] = None
    scoring_method: ScoringMethod
    test_cases: List[TestCaseRequest] = Field(..., min_items=1)
    created_by: str
    bench_version: str
    created_at: datetime


class TestSuite(BaseModel):
    id: UUID
    name: str
    scoring_method: str
    last_run_time: Optional[datetime] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class TestCaseOutput(BaseModel):
    """
    A generated output, score pair
    """
    id: Optional[UUID] = None
    """
    Optional unique identifier for this test case of the suite and run
    """
    output: Optional[str] = None
    """
    Generated output for test case
    """
    score: Optional[float] = None
    """
    Score assigned to output
    """


class CreateRunRequest(BaseModel):
    name: str
    """
    Name identifier of the run
    """
    test_case_outputs: List[TestCaseOutput]
    """
    List of outputs and scores for all cases in the test suite
    """
    created_by: str
    bench_version: str
    created_at: datetime
    description: Optional[str] = None
    """
    Optional description of the run
    """
    model_name: Optional[str] = None
    """
    Optional model name identifying the model used to generate outputs
    """
    foundation_model: Optional[str] = None
    """
    Optional foundation model name identifiying the pretrained model used to generate outputs
    """
    prompt_template: Optional[str] = None
    """
    Optional prompt template name identifying the global prompt used to generate outputs
    """
    model_version: Optional[str] = None
    """
    Optional model version identifying the version of the model used to generate outputs
    """


class TestRun(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_version: Optional[str] = None
    prompt_template: Optional[str] = None
    avg_score: Optional[float] = None


class PaginatedGetTestSuitesResponse(BaseModel):
    test_suites: Optional[List[TestSuite]] = None
    page: Optional[Page] = None
    page_size: Optional[PageSize] = None
    total_pages: Optional[TotalPages] = None
    total_count: Optional[TotalCount] = None


class TestCaseResponseItem(BaseModel):
    id: Optional[UUID] = None
    input: Optional[str] = None
    """
    Input to the test case. Does not include the prompt template.
    """
    reference_output: Optional[str] = None
    """
    Reference or "Golden" output for the given input.
    """


class HistogramItem(BaseModel):
    count: Optional[int] = None
    low: Optional[float] = None
    high: Optional[float] = None


class SummaryItem(BaseModel):
    id: Optional[UUID] = None
    avg_score: Optional[float] = None
    histogram: Optional[List[HistogramItem]] = None


class TestSuiteSummaryResponse(BaseModel):
    summary: Optional[List[SummaryItem]] = None
    page: Optional[Page] = None
    page_size: Optional[PageSize] = None
    total_pages: Optional[TotalPages] = None
    total_count: Optional[TotalCount] = None


class TestSuiteCase(BaseModel):
    id: Optional[UUID] = None
    input: Optional[str] = None
    reference_output: Optional[str] = None


class PaginatedGetTestSuiteResponse(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    scoring_method: Optional[str] = None
    test_cases: Optional[List[TestSuiteCase]] = None


class CreateRunResponse(BaseModel):
    id: Optional[UUID] = None


class RunResult(BaseModel):
    id: Optional[str] = None
    input: Optional[str] = None
    reference_output: Optional[str] = None
    output: Optional[str] = None
    score: Optional[float] = None


class PaginatedGetRunsForTestSuiteResponse(BaseModel):
    """
    Paginated list of runs for a test suite.
    """

    test_runs: List[TestRun]
    page: Optional[Page] = None
    page_size: Optional[PageSize] = None
    total_pages: Optional[TotalPages] = None
    total_count: Optional[TotalCount] = None


class PaginatedGetRunResponse(BaseModel):
    """
    Paginated list of prompts, reference outputs, and model outputs for a particular run.
    """

    test_case_runs: Optional[List[RunResult]] = None
    test_suite_id: Optional[UUID] = None
    page: Page
    page_size: PageSize
    total_pages: Optional[TotalPages] = None
    total_count: Optional[TotalCount] = None


class TestSuiteResponse(BaseModel):
    id: UUID
    name: str
    test_cases: List[TestCaseResponseItem] = Field(..., min_items=1)
    scoring_method: ScoringMethod
    description: Optional[str] = None
    organization_id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    """
    JSON object containing test case data for the test suite.
    """

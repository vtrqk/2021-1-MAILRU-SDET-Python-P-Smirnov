import pytest
from tests.base import BaseCase


class TestPopulationAndCalculator(BaseCase):

    @pytest.mark.AndroidUI_Population
    def test_search_population(self):
        self.main_page.send_text_to_search(word_to_search='Russia')
        self.main_page.check_search_results(check_text='Росси́йская Федера́ция')
        self.main_page.check_population(population='146')

    @pytest.mark.AndroidUI_Calculator
    def test_calculator(self):
        self.main_page.send_expression_and_check_result(expression='2+2*2', result='6')


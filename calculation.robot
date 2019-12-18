| *** Settings *** |
| Documentation  | Example of Robot file. |
| Library        | sum.py |
| Library        | multiply.py |

| *** Variables *** |
| ${iRet}         | ${EMPTY} |
| ${output}         | ${EMPTY} |

| *** Test Cases *** |

| SUM_TEST |
|	 | [Tags] | SUM_TEST |
|    | ${output}=     | sum test |
|    | Run Keyword If | '${output}' == 'FAIL' | FAIL |

| MULTIPLY_TEST |
|	 | [Tags] | MULTIPLY_TEST |
|    | ${output}=     | multiply test |
|    | Run Keyword If | '${output}' == 'FAIL' | FAIL |

| *** Keywords *** |

| sum test |
|    | ${iRet} =   | sum_calculation |
|    | [Return]    | ${iRet} |

| multiply test |
|    | ${iRet} =   | multiply_calculation |
|    | [Return]    | ${iRet} |
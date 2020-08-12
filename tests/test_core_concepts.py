import unittest
from airflow.models import DagBag


class TestCoreConceptsDAG(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag()
        self.dag = self.dagbag.get_dag(dag_id="core_concepts")

    def test_dag_loaded(self):
        self.assertDictEqual(self.dagbag.import_errors, {})
        self.assertIsNotNone(self.dag)

    def test_contain_tasks(self):
        self.assertListEqual(self.dag.task_ids, ["bash_command", "python_function"])

    def test_dependencies_of_bash_command(self):
        bash_task = self.dag.get_task("bash_command")

        self.assertEqual(bash_task.upstream_task_ids, set())
        self.assertEqual(bash_task.downstream_task_ids, set(["python_function"]))

    def assertDagDictEqual(self, structure, dag):
        self.assertEqual(dag.task_dict.keys(), structure.keys())

        for task_id, downstream_list in structure.items():
            self.assertTrue(dag.has_task(task_id))

            task = dag.get_task(task_id)

            self.assertEqual(task.downstream_task_ids, set(downstream_list))

    def test_dag_structure(self):
        self.assertDagDictEqual(
            {"bash_command": ["python_function"], "python_function": []}, self.dag
        )


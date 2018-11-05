from os import path
from mock import sentinel
from sceptre.context import SceptreContext


class TestSceptreContext(object):

    def setup_method(self, test_method):
        self.templates_path = "templates"
        self.config_path = "config"
        self.config_file = "config.yaml"

    def test_context_with_path(self):
        self.context = SceptreContext(
            project_path="project_path/to/sceptre",
            command_path=sentinel.command_path,
            user_variables=sentinel.user_variables,
            options=sentinel.options,
            output_format=sentinel.output_format,
            no_color=sentinel.no_color
        )

        sentinel.project_path = "project_path/to/sceptre"
        assert self.context.project_path == sentinel.project_path

    def test_full_config_path_returns_correct_path(self):
        context = SceptreContext(
            project_path="project_path",
            command_path=sentinel.command_path,
            user_variables=sentinel.user_variables,
            options=sentinel.options,
            output_format=sentinel.output_format,
            no_color=sentinel.no_color
        )

        full_config_path = path.join("project_path", self.config_path)
        assert context.full_config_path() == full_config_path

    def test_full_command_path_returns_correct_path(self):
        context = SceptreContext(
            project_path="project_path",
            command_path="command",
            user_variables=sentinel.user_variables,
            options=sentinel.options,
            output_format=sentinel.output_format,
            no_color=sentinel.no_color
        )
        full_command_path = path.join("project_path",
                                      self.config_path,
                                      "command")

        assert context.full_command_path() == full_command_path

    def test_full_templates_path_returns_correct_path(self):
        context = SceptreContext(
            project_path="project_path",
            command_path="command",
            user_variables=sentinel.user_variables,
            options=sentinel.options,
            output_format=sentinel.output_format,
            no_color=sentinel.no_color
        )
        full_templates_path = path.join("project_path", self.templates_path)
        assert context.full_templates_path() == full_templates_path

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Update(AAZCommand):
    """Update an attestation at resource scope.
    """

    _aaz_info = {
        "version": "2022-09-01",
        "resources": [
            ["mgmt-plane", "/{resourceid}/providers/microsoft.policyinsights/attestations/{}", "2022-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.attestation_name = AAZStrArg(
            options=["--attestation-name"],
            help="The name of the attestation.",
            required=True,
        )
        _args_schema.resource_id = AAZStrArg(
            options=["--resource-id"],
            help="Resource ID.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.assessment_date = AAZDateTimeArg(
            options=["--assessment-date"],
            arg_group="Properties",
            help="The time the evidence was assessed",
            nullable=True,
        )
        _args_schema.comments = AAZStrArg(
            options=["--comments"],
            arg_group="Properties",
            help="Comments describing why this attestation was created.",
            nullable=True,
        )
        _args_schema.compliance_state = AAZStrArg(
            options=["--compliance-state"],
            arg_group="Properties",
            help="The compliance state that should be set on the resource.",
            nullable=True,
            enum={"Compliant": "Compliant", "NonCompliant": "NonCompliant", "Unknown": "Unknown"},
        )
        _args_schema.evidence = AAZListArg(
            options=["--evidence"],
            arg_group="Properties",
            help="The evidence supporting the compliance state set in this attestation.",
            nullable=True,
        )
        _args_schema.expires_on = AAZDateTimeArg(
            options=["--expires-on"],
            arg_group="Properties",
            help="The time the compliance state should expire.",
            nullable=True,
        )
        _args_schema.metadata = AAZDictArg(
            options=["--metadata"],
            arg_group="Properties",
            help="Additional metadata for this attestation",
            nullable=True,
        )
        _args_schema.owner = AAZStrArg(
            options=["--owner"],
            arg_group="Properties",
            help="The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.",
            nullable=True,
        )
        _args_schema.policy_assignment_id = AAZStrArg(
            options=["--policy-assignment-id"],
            arg_group="Properties",
            help="The resource ID of the policy assignment that the attestation is setting the state for.",
        )
        _args_schema.policy_definition_reference_id = AAZStrArg(
            options=["--policy-definition-reference-id"],
            arg_group="Properties",
            help="The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.",
            nullable=True,
        )

        evidence = cls._args_schema.evidence
        evidence.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.evidence.Element
        _element.description = AAZStrArg(
            options=["description"],
            help="The description for this piece of evidence.",
            nullable=True,
        )
        _element.source_uri = AAZStrArg(
            options=["source-uri"],
            help="The URI location of the evidence.",
            nullable=True,
        )

        metadata = cls._args_schema.metadata
        metadata.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AttestationsGetAtResource(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AttestationsCreateOrUpdateAtResource(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AttestationsGetAtResource(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{resourceId}/providers/Microsoft.PolicyInsights/attestations/{attestationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "attestationName", self.ctx.args.attestation_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceId", self.ctx.args.resource_id,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_attestation_read(cls._schema_on_200)

            return cls._schema_on_200

    class AttestationsCreateOrUpdateAtResource(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{resourceId}/providers/Microsoft.PolicyInsights/attestations/{attestationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "attestationName", self.ctx.args.attestation_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceId", self.ctx.args.resource_id,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_attestation_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("assessmentDate", AAZStrType, ".assessment_date")
                properties.set_prop("comments", AAZStrType, ".comments")
                properties.set_prop("complianceState", AAZStrType, ".compliance_state")
                properties.set_prop("evidence", AAZListType, ".evidence")
                properties.set_prop("expiresOn", AAZStrType, ".expires_on")
                properties.set_prop("metadata", AAZDictType, ".metadata")
                properties.set_prop("owner", AAZStrType, ".owner")
                properties.set_prop("policyAssignmentId", AAZStrType, ".policy_assignment_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("policyDefinitionReferenceId", AAZStrType, ".policy_definition_reference_id")

            evidence = _builder.get(".properties.evidence")
            if evidence is not None:
                evidence.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.evidence[]")
            if _elements is not None:
                _elements.set_prop("description", AAZStrType, ".description")
                _elements.set_prop("sourceUri", AAZStrType, ".source_uri")

            metadata = _builder.get(".properties.metadata")
            if metadata is not None:
                metadata.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_attestation_read = None

    @classmethod
    def _build_schema_attestation_read(cls, _schema):
        if cls._schema_attestation_read is not None:
            _schema.id = cls._schema_attestation_read.id
            _schema.name = cls._schema_attestation_read.name
            _schema.properties = cls._schema_attestation_read.properties
            _schema.system_data = cls._schema_attestation_read.system_data
            _schema.type = cls._schema_attestation_read.type
            return

        cls._schema_attestation_read = _schema_attestation_read = AAZObjectType()

        attestation_read = _schema_attestation_read
        attestation_read.id = AAZStrType(
            flags={"read_only": True},
        )
        attestation_read.name = AAZStrType(
            flags={"read_only": True},
        )
        attestation_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        attestation_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        attestation_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_attestation_read.properties
        properties.assessment_date = AAZStrType(
            serialized_name="assessmentDate",
        )
        properties.comments = AAZStrType()
        properties.compliance_state = AAZStrType(
            serialized_name="complianceState",
        )
        properties.evidence = AAZListType()
        properties.expires_on = AAZStrType(
            serialized_name="expiresOn",
        )
        properties.last_compliance_state_change_at = AAZStrType(
            serialized_name="lastComplianceStateChangeAt",
            flags={"read_only": True},
        )
        properties.metadata = AAZDictType()
        properties.owner = AAZStrType()
        properties.policy_assignment_id = AAZStrType(
            serialized_name="policyAssignmentId",
            flags={"required": True},
        )
        properties.policy_definition_reference_id = AAZStrType(
            serialized_name="policyDefinitionReferenceId",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        evidence = _schema_attestation_read.properties.evidence
        evidence.Element = AAZObjectType()

        _element = _schema_attestation_read.properties.evidence.Element
        _element.description = AAZStrType()
        _element.source_uri = AAZStrType(
            serialized_name="sourceUri",
        )

        metadata = _schema_attestation_read.properties.metadata
        metadata.Element = AAZStrType()

        system_data = _schema_attestation_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_attestation_read.id
        _schema.name = cls._schema_attestation_read.name
        _schema.properties = cls._schema_attestation_read.properties
        _schema.system_data = cls._schema_attestation_read.system_data
        _schema.type = cls._schema_attestation_read.type


__all__ = ["Update"]

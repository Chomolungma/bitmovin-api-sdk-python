# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.web_vtt_extract import WebVttExtract
from bitmovin.encoding.encodings.captions.extract.webvtt.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.captions.extract.webvtt.web_vtt_extract_list_query_params import WebVttExtractListQueryParams


class WebvttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WebvttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, web_vtt_extract, **kwargs):
        """Extract WebVtt Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/extract/webvtt',
            web_vtt_extract,
            path_params={'encoding_id': encoding_id},
            type=WebVttExtract,
            **kwargs
        )

    def delete(self, encoding_id, captions_id, **kwargs):
        """Delete Extract WebVtt Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/extract/webvtt/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=WebVttExtract,
            **kwargs
        )

    def get(self, encoding_id, captions_id, **kwargs):
        """Get Extract WebVtt Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/extract/webvtt/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=WebVttExtract,
            **kwargs
        )

    def list(self, encoding_id, query_params: WebVttExtractListQueryParams = None, **kwargs):
        """List Extract WebVtt Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/extract/webvtt',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=WebVttExtract,
            **kwargs
        )
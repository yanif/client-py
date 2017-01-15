#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.10757 (http://hl7.org/fhir/StructureDefinition/Catalog) on 2017-01-15.
#  2017, SMART Health IT.


from . import domainresource

class Catalog(domainresource.DomainResource):
    """ Catalog document.
    
    A document that bundles a set of catalog entries: items (that can be
    ordered or referenced) and their characteristics.
    """
    
    resource_type = "Catalog"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.document = None
        """ Properties of the document - authorship, versions, etc.
        Type `CatalogDocument` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier for the  catalog resource.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.item = None
        """ Each item of the catalog.
        List of `CatalogItem` items (represented as `dict` in JSON). """
        
        super(Catalog, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Catalog, self).elementProperties()
        js.extend([
            ("document", "document", CatalogDocument, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("item", "item", CatalogItem, True, None, True),
        ])
        return js


from . import backboneelement

class CatalogDocument(backboneelement.BackboneElement):
    """ Properties of the document - authorship, versions, etc.
    """
    
    resource_type = "CatalogDocument"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ The type of content in the document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contentVersion = None
        """ The version of the catalog content.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier for the catalog document.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issueDate = None
        """ The date when the catalog document is issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.provider = None
        """ The entity that is issuing (sending, submitting, publishing) the
        catalog.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.status = None
        """ Status of the catalog document: pre-submission, pending, approved,
        draft.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.updateMode = None
        """ How the content is intended to be used - overwriting, appending,
        complementing existing items.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validFrom = None
        """ The date from which the catalog content is expected to be active.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.validTo = None
        """ The date until which the catalog content is expected to be active.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(CatalogDocument, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogDocument, self).elementProperties()
        js.extend([
            ("contentType", "contentType", codeableconcept.CodeableConcept, False, None, True),
            ("contentVersion", "contentVersion", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issueDate", "issueDate", fhirdate.FHIRDate, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("updateMode", "updateMode", codeableconcept.CodeableConcept, False, None, True),
            ("validFrom", "validFrom", fhirdate.FHIRDate, False, None, False),
            ("validTo", "validTo", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class CatalogItem(backboneelement.BackboneElement):
    """ Each item of the catalog.
    """
    
    resource_type = "CatalogItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalCharacteristic = None
        """ Additional characteristics of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.additionalClassification = None
        """ Additional classification of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.additionalIdentifier = None
        """ Any additional identifier(s) for the catalog item, in the same
        granularity or concept.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.classification = None
        """ Classification of the item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier of the catalog item.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.lastUpdated = None
        """ Perhaps not needed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.referencedItem = None
        """ The item itself.
        Type `FHIRReference` referencing `Medication, Device, Procedure, CarePlan, Organization, Practitioner, HealthcareService, ServiceDefinition` (represented as `dict` in JSON). """
        
        self.relatedItem = None
        """ An item that this catalog entry is related to.
        List of `CatalogItemRelatedItem` items (represented as `dict` in JSON). """
        
        self.status = None
        """ The status of the item, e.g. active, approved….
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of item - medication, device, service, protocol or other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validFrom = None
        """ The date from which this catalog entry is expected to be active.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.validTo = None
        """ The date until which this catalog entry is expected to be active.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(CatalogItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogItem, self).elementProperties()
        js.extend([
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, True, None, False),
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, True, None, False),
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, True, None, False),
            ("classification", "classification", identifier.Identifier, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, False),
            ("relatedItem", "relatedItem", CatalogItemRelatedItem, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("validFrom", "validFrom", fhirdate.FHIRDate, False, None, False),
            ("validTo", "validTo", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class CatalogItemRelatedItem(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.
    
    Used for example,  to point to a substance, or to a device used to
    administer a medication.
    """
    
    resource_type = "CatalogItemRelatedItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ The reference to the related item.
        Type `FHIRReference` referencing `Medication, Device, Procedure, CarePlan, Organization, Practitioner, HealthcareService, ServiceDefinition` (represented as `dict` in JSON). """
        
        self.relationtype = None
        """ The type of relation to the related item.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of related item.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CatalogItemRelatedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogItemRelatedItem, self).elementProperties()
        js.extend([
            ("identifier", "identifier", fhirreference.FHIRReference, False, None, True),
            ("relationtype", "relationtype", codeableconcept.CodeableConcept, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier

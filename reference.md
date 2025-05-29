# Reference
## Contract
<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">generate_contract</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a new contract object from a Base64 encoded PDF of a contract. This endpoint will block until the contract is generated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.contract_types import GenerateContractRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.generate_contract(
    request=GenerateContractRequest(
        document="data:application/pdf;base64,JVBERi0xLjEKJcKlwrHDqwoKMSAwIG9iagogIDw8IC9UeXBlIC9DYXRhbG9nCiAgICAgL1BhZ2VzIDIgMCBSCiAgPj4KZW5kb2JqCgoyIDAgb2JqCiAgPDwgL1R5cGUgL1BhZ2VzCiAgICAgL0tpZHMgWzMgMCBSXQogICAgIC9Db3VudCAxCiAgICAgL01lZGlhQm94IFswIDAgMzAwIDE0NF0KICA+PgplbmRvYmoKCjMgMCBvYmoKICA8PCAgL1R5cGUgL1BhZ2UKICAgICAgL1BhcmVudCAyIDAgUgogICAgICAvUmVzb3VyY2VzCiAgICAgICA8PCAvRm9udAogICAgICAgICAgIDw8IC9GMQogICAgICAgICAgICAgICA8PCAvVHlwZSAvRm9udAogICAgICAgICAgICAgICAgICAvU3VidHlwZSAvVHlwZTEKICAgICAgICAgICAgICAgICAgL0Jhc2VGb250IC9UaW1lcy1Sb21hbgogICAgICAgICAgICAgICA+PgogICAgICAgICAgID4+CiAgICAgICA+PgogICAgICAvQ29udGVudHMgNCAwIFIKICA+PgplbmRvYmoKCjQgMCBvYmoKICA8PCAvTGVuZ3RoIDU1ID4+CnN0cmVhbQogIEJUCiAgICAvRjEgMTggVGYKICAgIDAgMCBUZAogICAgKEhlbGxvIFdvcmxkKSBUagogIEVUCmVuZHN0cmVhbQplbmRvYmoKCnhyZWYKMCA1CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxOCAwMDAwMCBuIAowMDAwMDAwMDc3IDAwMDAwIG4gCjAwMDAwMDAxNzggMDAwMDAgbiAKMDAwMDAwMDQ1NyAwMDAwMCBuIAp0cmFpbGVyCiAgPDwgIC9Sb290IDEgMCBSCiAgICAgIC9TaXplIDUKICA+PgpzdGFydHhyZWYKNTY1CiUlRU9GCg==",
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `GenerateContractRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">generate_contract_run_async</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a new contract object from a Base64 encoded PDF of a contract. This endpoint will return immediately and the contract will be generated asynchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.contract_types import GenerateContractRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.generate_contract_run_async(
    request=GenerateContractRequest(
        document="data:application/pdf;base64,JVBERi0xLjEKJcKlwrHDqwoKMSAwIG9iagogIDw8IC9UeXBlIC9DYXRhbG9nCiAgICAgL1BhZ2VzIDIgMCBSCiAgPj4KZW5kb2JqCgoyIDAgb2JqCiAgPDwgL1R5cGUgL1BhZ2VzCiAgICAgL0tpZHMgWzMgMCBSXQogICAgIC9Db3VudCAxCiAgICAgL01lZGlhQm94IFswIDAgMzAwIDE0NF0KICA+PgplbmRvYmoKCjMgMCBvYmoKICA8PCAgL1R5cGUgL1BhZ2UKICAgICAgL1BhcmVudCAyIDAgUgogICAgICAvUmVzb3VyY2VzCiAgICAgICA8PCAvRm9udAogICAgICAgICAgIDw8IC9GMQogICAgICAgICAgICAgICA8PCAvVHlwZSAvRm9udAogICAgICAgICAgICAgICAgICAvU3VidHlwZSAvVHlwZTEKICAgICAgICAgICAgICAgICAgL0Jhc2VGb250IC9UaW1lcy1Sb21hbgogICAgICAgICAgICAgICA+PgogICAgICAgICAgID4+CiAgICAgICA+PgogICAgICAvQ29udGVudHMgNCAwIFIKICA+PgplbmRvYmoKCjQgMCBvYmoKICA8PCAvTGVuZ3RoIDU1ID4+CnN0cmVhbQogIEJUCiAgICAvRjEgMTggVGYKICAgIDAgMCBUZAogICAgKEhlbGxvIFdvcmxkKSBUagogIEVUCmVuZHN0cmVhbQplbmRvYmoKCnhyZWYKMCA1CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxOCAwMDAwMCBuIAowMDAwMDAwMDc3IDAwMDAwIG4gCjAwMDAwMDAxNzggMDAwMDAgbiAKMDAwMDAwMDQ1NyAwMDAwMCBuIAp0cmFpbGVyCiAgPDwgIC9Sb290IDEgMCBSCiAgICAgIC9TaXplIDUKICA+PgpzdGFydHhyZWYKNTY1CiUlRU9GCg==",
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `GenerateContractRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">generate_contract_get_async</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status and results of an asynchronous contract generation job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.generate_contract_get_async(
    job_id="cntgen_d6734204-ae46-4fe9-a0c5-bd2763d40c9b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `ContractJobId` — Job ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">preview_invoices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate previews of the invoices that will be created from the provided contract.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.contract_types import (
    ContractCreateRequest,
    ContractInvoiceLineItemSchema,
    ContractInvoiceSchema,
    ContractRecurrenceCreateRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.preview_invoices(
    contract=ContractCreateRequest(
        summary="Contract Start Date: January 29, 2025\nParties to the Agreement:\n- Provider (Vendor): [Vendor Name] - Client (Payer): [Client Name]\nFees and Payment Terms:\n- Monthly Recurring Fee: \\$20.00 - Payment Schedule: Fees are payable in advance on the 1st day of each month. - First Payment Date: February 1, 2025 - Payment Method: Via credit card to the account designated by Provider. - Payment Due Date: Payment is due 5 days after the invoice date.\n",
        recurrences=[
            ContractRecurrenceCreateRequest(
                rrule="DTSTART:20250201T000000ZRRULE:FREQ=MONTHLY;INTERVAL=1;BYMONTHDAY=1",
                justification="Monthly recurring fee billed in advance on the 1st of each month",
                filtered_contract_summary="Contract Start Date: January 29, 2025\nParties to the Agreement:\n- Provider (Vendor): [Vendor Name] - Client (Payer): [Client Name]\nFees and Payment Terms:\n- Monthly Recurring Fee: \\$20.00 - Payment Schedule: Fees are payable in advance on the 1st day of each month. - First Payment Date: February 1, 2025 - Payment Method: Via credit card to the account designated by Provider. - Payment Due Date: Payment is due 5 days after the invoice date.\n",
                invoice_schema=ContractInvoiceSchema(
                    line_items=[
                        ContractInvoiceLineItemSchema(
                            name="Monthly Subscription Service Fee",
                            unit_price=20.0,
                            currency="USD",
                            quantity=1.0,
                        )
                    ],
                ),
            )
        ],
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    ),
    invoice_indexes=[0],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract:** `ContractCreateRequest` — Contract to preview invoice creation for
    
</dd>
</dl>

<dl>
<dd>

**invoice_indexes:** `typing.Sequence[int]` — Indexes of the invoices to generate from each recurrence (e.g. [0, 1, 2] for the first three invoices).  Note that contracts with multiple recurrences will generate more preview invoices, and invalid invoice indexes will be ignored silently. For example, [0, 1, 2] on a contract with 2 recurrences will generate at most 6 invoices, and potentially fewer if some of indexes are out of bounds for a recurrence.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">apply_contract_feedback</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply feedback to a contract, generating an updated contract object.  NOTE: This works by re-extracting the contract details with the provided feedback in mind.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.apply_contract_feedback(
    contract_id="cnt_3bd62b69-3835-433e-829f-4388a2e46c41",
    feedback="Change the monthly fee to $20.00",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` — Contract ID
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `str` — Natural language feedback to apply to the contract
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">apply_invoice_feedback</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply feedback to an invoice, generating an updated invoice object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.apply_invoice_feedback(
    contract_id="cnt_3bd62b69-3835-433e-829f-4388a2e46c41",
    feedback="There were 2 subscriptions this month",
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` — Contract ID
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `str` — Natural language feedback to apply to the invoice
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `InvoiceId` — ID of the invoice to apply feedback to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search contracts for all entities in the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.find(
    creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**creator_entity_id:** `typing.Optional[EntityId]` — ID of the entity that created the contracts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.contract_types import (
    ContractCreateRequest,
    ContractInvoiceLineItemSchema,
    ContractInvoiceSchema,
    ContractRecurrenceCreateRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.create(
    request=ContractCreateRequest(
        summary="Contract Start Date: January 29, 2025\nParties to the Agreement:\n- Provider (Vendor): [Vendor Name] - Client (Payer): [Client Name]\nFees and Payment Terms:\n- Monthly Recurring Fee: \\$20.00 - Payment Schedule: Fees are payable in advance on the 1st day of each month. - First Payment Date: February 1, 2025 - Payment Method: Via credit card to the account designated by Provider. - Payment Due Date: Payment is due 5 days after the invoice date.\n",
        recurrences=[
            ContractRecurrenceCreateRequest(
                rrule="DTSTART:20250201T000000ZRRULE:FREQ=MONTHLY;INTERVAL=1;BYMONTHDAY=1",
                justification="Monthly recurring fee billed in advance on the 1st of each month",
                filtered_contract_summary="Contract Start Date: January 29, 2025\nParties to the Agreement:\n- Provider (Vendor): [Vendor Name] - Client (Payer): [Client Name]\nFees and Payment Terms:\n- Monthly Recurring Fee: \\$20.00 - Payment Schedule: Fees are payable in advance on the 1st day of each month. - First Payment Date: February 1, 2025 - Payment Method: Via credit card to the account designated by Provider. - Payment Due Date: Payment is due 5 days after the invoice date.\n",
                invoice_schema=ContractInvoiceSchema(
                    line_items=[
                        ContractInvoiceLineItemSchema(
                            name="Monthly Subscription Service Fee",
                            unit_price=20.0,
                            currency="USD",
                            quantity=1.0,
                        )
                    ],
                ),
            )
        ],
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ContractCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.get(
    contract_id="cnt_3bd62b69-3835-433e-829f-4388a2e46c41",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` — Contract ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.contract_types import (
    ContractInvoiceLineItemSchema,
    ContractInvoiceSchema,
    ContractRecurrenceCreateRequest,
    ContractUpdateRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.update(
    contract_id="cnt_3bd62b69-3835-433e-829f-4388a2e46c41",
    request=ContractUpdateRequest(
        summary="Contract Start Date: January 29, 2025\nParties to the Agreement:\n- Provider (Vendor): [Vendor Name] - Client (Payer): [Client Name]\nFees and Payment Terms:\n- Monthly Recurring Fee: \\$20.00 - Payment Schedule: Fees are payable in advance on the 1st day of each month. - First Payment Date: February 1, 2025 - Payment Method: Via credit card to the account designated by Provider. - Payment Due Date: Payment is due 5 days after the invoice date.\n",
        recurrences=[
            ContractRecurrenceCreateRequest(
                rrule="DTSTART:20250201T000000ZRRULE:FREQ=MONTHLY;INTERVAL=1;BYMONTHDAY=1",
                justification="Monthly recurring fee billed in advance on the 1st of each month",
                filtered_contract_summary="Contract Start Date: January 29, 2025\nParties to the Agreement:\n- Provider (Vendor): [Vendor Name] - Client (Payer): [Client Name]\nFees and Payment Terms:\n- Monthly Recurring Fee: \\$20.00 - Payment Schedule: Fees are payable in advance on the 1st day of each month. - First Payment Date: February 1, 2025 - Payment Method: Via credit card to the account designated by Provider. - Payment Due Date: Payment is due 5 days after the invoice date.\n",
                invoice_schema=ContractInvoiceSchema(
                    line_items=[
                        ContractInvoiceLineItemSchema(
                            name="Monthly Subscription Service Fee",
                            unit_price=20.0,
                            currency="USD",
                            quantity=1.0,
                        )
                    ],
                ),
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` — Contract ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContractUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contract.<a href="src/mercoa/contract/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.contract.delete(
    contract_id="cnt_3bd62b69-3835-433e-829f-4388a2e46c41",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` — Contract ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EntityGroup
<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all entity groups. If using a JWT, will return all groups the entity is part of. If using an API key, will return all groups for the organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return. Defaults to 1. Max is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityGroupId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupCreateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.create(
    request=EntityGroupCreateRequest(
        foreign_id="your-group-id",
        name="Coastal Corporation",
        email_to_name="coastalcorp",
        entity_ids=[
            "ent_e8c2af94-61cd-4036-a765-80341209167b",
            "ent_1176dd0c-12e1-41c7-85a5-ae9b4746e64b",
            "ent_3dbb4ede-2d1d-49be-a996-a5dfad3641be",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EntityGroupCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get(
    entity_group_id="entg_a3582b70-fd04-4888-9185-a640ae9048be",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**return_entity_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities in the group. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.update(
    entity_group_id="entg_a3582b70-fd04-4888-9185-a640ae9048be",
    request=EntityGroupUpdateRequest(
        foreign_id="your-group-id",
        name="AcmeConglomerate",
        email_to_name="acmegroup",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.delete(
    entity_group_id="entityGroupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity group with the given options. This token can be used to authenticate to any entity in the entity group in the Mercoa API and iFrame.

<Warning>We recommend using [this endpoint](/api-reference/entity-group/user/get-token). This will enable features such as approvals and comments.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get_token(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
        session_id="session_123",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">add_entities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add entities to an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupAddEntitiesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.add_entities(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityGroupAddEntitiesRequest(
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
        copy_users_from="ent_1176dd0c-12e1-41c7-85a5-ae9b4746e64b",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupAddEntitiesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">remove_entities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove entities from an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupRemoveEntitiesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.remove_entities(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityGroupRemoveEntitiesRequest(
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupRemoveEntitiesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EntityGroup User
<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search entity group users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.find(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    name="John",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter users by role. If multiple roles are provided, users with any of the roles will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter users by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter users by email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityUserId]` — The ID of the user to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create entity user that will be added to all entities in the group. If a user with the same foreignId already exists, the user will be updated with the new information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import (
    EntityGroupUserEntityRequest,
    EntityGroupUserRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.create(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityGroupUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        entities=[
            EntityGroupUserEntityRequest(
                roles=["admin", "approver"],
                entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            ),
            EntityGroupUserEntityRequest(
                roles=["viewer"],
                entity_id="ent_9e02a20e-7749-47de-8d8a-f8ff2859fa90",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity user from a group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.get(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    foreign_id="MY-DB-ID-12345",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity user for all entities in the group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import (
    EntityGroupUserEntityRequest,
    EntityGroupUserRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.update(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    foreign_id="MY-DB-ID-12345",
    request=EntityGroupUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        entities=[
            EntityGroupUserEntityRequest(
                roles=["admin", "approver"],
                entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            ),
            EntityGroupUserEntityRequest(
                roles=["viewer"],
                entity_id="ent_9e02a20e-7749-47de-8d8a-f8ff2859fa90",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity user from all entities in the group. This will also remove the user from all approval policies. If an approval policy will break as a result of this operation, this request will fail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.delete(
    entity_group_id="entityGroupId",
    foreign_id="foreignId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity group with the given options. This token can be used to authenticate to any entity in the entity group as the user in the Mercoa API and iFrame.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.get_token(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    foreign_id="MY-DB-ID-12345",
    request=TokenGenerationOptions(
        expires_in="1h",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync entity group users. This will add users to entities that do not have them and remove users from entities that have them.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupUserSyncRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.sync(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityGroupUserSyncRequest(
        filter_roles=["approver", "viewer"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserSyncRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity
<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all entities with the given filters. If no filters are provided, all entities will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.find(
    is_customer=True,
    foreign_id="MY-DB-ID-12345",
    payment_methods=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — If true, will include entity payment methods as part of the response
    
</dd>
</dl>

<dl>
<dd>

**is_customer:** `typing.Optional[bool]` — If true, only entities with a direct relationship to the requesting organization will be returned. If false or not provided, all entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify this entity in your system
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[EntityStatus, typing.Sequence[EntityStatus]]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_payee:** `typing.Optional[bool]` 

If true, entities that are marked as payees will be returned.
If false or not provided, entities that are marked as payees will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**is_payor:** `typing.Optional[bool]` 

If true or not provided, entities that are marked as payors will be returned.
If false, entities that are marked as payors will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Use search instead. Deprecated. Filter entities by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find entities by name, email, or emailTo. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[MetadataFilter]` — Filter entities by simple key/value metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the entity to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    BusinessProfileRequest,
    EntityCreationRequest,
    ProfileRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.create(
    request=EntityCreationRequest(
        is_customer=False,
        is_payor=False,
        is_payee=True,
        account_type="business",
        foreign_id="MY-DB-ID-90909",
        profile=ProfileRequest(
            business=BusinessProfileRequest(
                email="vendor@bigboxstore.com",
                legal_business_name="Big Box Store",
                website="http://www.bigboxstore.com",
                business_type="publicCorporation",
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EntityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.commons import Address, PhoneNumber
from mercoa.entity_types import (
    BusinessProfileRequest,
    Ein,
    EntityUpdateRequest,
    ProfileRequest,
    TaxId,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityUpdateRequest(
        is_customer=True,
        is_payor=True,
        is_payee=False,
        account_type="business",
        foreign_id="MY-DB-ID-12345",
        profile=ProfileRequest(
            business=BusinessProfileRequest(
                email="customer@acme.com",
                legal_business_name="Acme Inc.",
                website="http://www.acme.com",
                business_type="llc",
                phone=PhoneNumber(
                    country_code="1",
                    number="4155551234",
                ),
                address=Address(
                    address_line_1="123 Main St",
                    address_line_2="Unit 1",
                    city="San Francisco",
                    state_or_province="CA",
                    postal_code="94105",
                    country="US",
                ),
                tax_id=TaxId(
                    ein=Ein(
                        number="12-3456789",
                    ),
                ),
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Will archive the entity. This action cannot be undone, and the entity will no longer be available for use. The foreignId on the entity will be cleared as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.delete(
    entity_id="entityId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">accept_terms_of_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to indicate acceptance of Mercoa's terms of service for an entity. Send a request to this endpoint only after the entity has accepted the Mercoa ToS. Entities must accept Mercoa ToS before they can be send or pay invoices using Mercoa's payment rails.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.accept_terms_of_service(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">initiate_kyb</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to initiate KYB for an entity. 
Send a request to this endpoint only after the entity has accepted the Mercoa ToS,
all representatives have been added, and all required fields have been filled out.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.initiate_kyb(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity with the given options. This token can be used to authenticate the entity in the Mercoa API and iFrame.

<Warning>We recommend using [this endpoint](/api-reference/entity/user/get-token). This will enable features such as approvals and comments.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get_token(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
        session_id="session_123",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get_onboarding_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an onboarding link for the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get_onboarding_link(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    type="PAYOR",
    expires_in="1h",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntityOnboardingLinkType` — The type of onboarding link to generate. If not provided, the default is payee. The onboarding options are determined by your organization's onboarding configuration.
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 24h.
    
</dd>
</dl>

<dl>
<dd>

**connected_entity_id:** `typing.Optional[EntityId]` — The ID of the entity to connect to. If onboarding a payee, this should be the payor entity ID. If onboarding a payor, this should be the payee entity ID. If no connected entity ID is provided, the onboarding link will be for a standalone entity.
    
</dd>
</dl>

<dl>
<dd>

**redirect_to_portal:** `typing.Optional[bool]` — If true, the onboarding link will redirect to the vendor/customer portal if the entity is already onboarded. If false, the onboarding link will not redirect to the portal. The default is false.
    
</dd>
</dl>

<dl>
<dd>

**vendor_portal_options:** `typing.Optional[VendorPortalOptions]` — The options for the vendor portal.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">send_onboarding_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an email with a onboarding link to the entity. The email will be sent to the email address associated with the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.send_onboarding_link(
    entity_id="entityId",
    type="PAYEE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntityOnboardingLinkType` — The type of onboarding link to generate. If not provided, the default is payee. The onboarding options are determined by your organization's onboarding configuration.
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**connected_entity_id:** `typing.Optional[EntityId]` — The ID of the entity to connect to. If onboarding a payee, this should be the payor entity ID. If onboarding a payor, this should be the payee entity ID. If no connected entity ID is provided, the onboarding link will be for a standalone entity.
    
</dd>
</dl>

<dl>
<dd>

**redirect_to_portal:** `typing.Optional[bool]` — If true, the onboarding link will redirect to the vendor/customer portal if the entity is already onboarded. If false, the onboarding link will not redirect to the portal. The default is false.
    
</dd>
</dl>

<dl>
<dd>

**vendor_portal_options:** `typing.Optional[VendorPortalOptions]` — The options for the vendor portal.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all events for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.events(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. If not provided, events from the start of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. If not provided, events to the end of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Limit can range between 1 and 100, and the default is 50.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityEventId]` — The ID of the event to start after. If not provided, the first page of events will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Counterparty
<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">find_payees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find payee counterparties. This endpoint lets you find vendors linked to the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.find_payees(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    name="Big Box",
    payment_methods=True,
    invoice_metrics=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Use search instead. Deprecated. Filter counterparties by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Filter counterparties by name or email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**network_type:** `typing.Optional[
    typing.Union[
        CounterpartyNetworkType, typing.Sequence[CounterpartyNetworkType]
    ]
]` — Filter by network type. By default, only ENTITY counterparties are returned.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — If true, will include counterparty payment methods as part of the response
    
</dd>
</dl>

<dl>
<dd>

**invoice_metrics:** `typing.Optional[bool]` — If true, will include counterparty invoice metrics as part of the response
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter by counterparty ids (Foreign ID is supported)
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter counterparties by simple key/value metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — If true, will return simple key/value metadata for the counterparties. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of counterparties to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the counterparties to start after. If not provided, the first page of counterparties will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">find_payors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find payor counterparties. This endpoint lets you find customers linked to the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.find_payors(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    name="Big Box",
    payment_methods=True,
    invoice_metrics=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Use search instead. Deprecated. Filter counterparties by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Filter counterparties by name or email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**network_type:** `typing.Optional[
    typing.Union[
        CounterpartyNetworkType, typing.Sequence[CounterpartyNetworkType]
    ]
]` — Filter by network type. By default, only ENTITY counterparties are returned.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — If true, will include counterparty payment methods as part of the response
    
</dd>
</dl>

<dl>
<dd>

**invoice_metrics:** `typing.Optional[bool]` — If true, will include counterparty invoice metrics as part of the response
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter by counterparty ids (Foreign ID is supported)
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter counterparties by simple key/value metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — If true, will return simple key/value metadata for the counterparties. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of counterparties to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the counterparties to start after. If not provided, the first page of counterparties will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">add_payees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create association between Entity and a given list of Payees. If a Payee has previously been archived, unarchive the Payee.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    CounterpartyCustomizationAccount,
    CounterpartyCustomizationRequest,
    EntityAddPayeesRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.add_payees(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityAddPayeesRequest(
        payees=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
        customizations=[
            CounterpartyCustomizationRequest(
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                accounts=[
                    CounterpartyCustomizationAccount(
                        account_id="85866843",
                        postal_code="94105",
                        name_on_account="John Doe",
                    )
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityAddPayeesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">hide_payees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks Payees as unsearchable by Entity via Counterparty search. Invoices associated with these Payees will still be searchable via Invoice search.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityHidePayeesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.hide_payees(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityHidePayeesRequest(
        payees=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityHidePayeesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">add_payors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create association between Entity and a given list of Payors. If a Payor has previously been archived, unarchive the Payor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    CounterpartyCustomizationAccount,
    CounterpartyCustomizationRequest,
    EntityAddPayorsRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.add_payors(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityAddPayorsRequest(
        payors=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
        customizations=[
            CounterpartyCustomizationRequest(
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                accounts=[
                    CounterpartyCustomizationAccount(
                        account_id="85866843",
                        postal_code="94105",
                        name_on_account="John Doe",
                    )
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityAddPayorsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">hide_payors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks Payors as unsearchable by Entity via Counterparty search. Invoices associated with these Payors will still be searchable via Invoice search.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityHidePayorsRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.hide_payors(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityHidePayorsRequest(
        payors=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityHidePayorsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity EmailLog
<details><summary><code>client.entity.email_log.<a href="src/mercoa/entity/email_log/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all incoming invoice emails for an entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_log.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of logs to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the log to start after. If not provided, the first page of logs will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search for logs by email address or subject
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.email_log.<a href="src/mercoa/entity/email_log/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an email log by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_log.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    log_id="log_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**log_id:** `EmailLogId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity PaymentMethod
<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    type="bankAccount",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[
    typing.Union[PaymentMethodType, typing.Sequence[PaymentMethodType]]
]` — Type of payment method to filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import PaymentMethodRequest_Wallet

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=PaymentMethodRequest_Wallet(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `PaymentMethodRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only custom payment methods can be updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import PaymentMethodUpdateRequest_BankAccount

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    request=PaymentMethodUpdateRequest_BankAccount(
        default_source=True,
        default_destination=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `PaymentMethodUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a payment method as inactive. This will not remove the payment method from the system, but will prevent it from being used in the future.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.delete(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">plaid_link_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a Plaid link token for an entity. This token can be used to add or update a bank account to the entity using Plaid Link.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.plaid_link_token(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `typing.Optional[PaymentMethodId]` — ID of Bank Account to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">card_link_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a card link token for an entity. This token is used by the frontend components to generate a PCI compliant form to add a card to the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.card_link_token(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.events(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. If not provided, events from the start of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. If not provided, events to the end of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of events returned. Limit can range between 1 and 100, and the default is 50.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[PaymentMethodEventId]` — The ID of the event to start after.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity User
<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search entity users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.find(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    name="John",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter users by role. If multiple roles are provided, users with any of the roles will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter users by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter users by email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityUserId]` — The ID of the user to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityUserRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.create(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        roles=["admin", "approver"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityUserRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
    request=EntityUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        roles=["admin", "approver"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity user. This will also remove the user from all approval policies. If an approval policy will break as a result of this operation, this request will fail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.delete(
    entity_id="entityId",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity user with the given options. This token can be used to authenticate the entity and entity user in the Mercoa API and iFrame.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.get_token(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
        session_id="session_123",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InvoiceTemplate
<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search invoice templates for all entities in the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoice templates by the ID or foreign ID of the entity that is the payer or the vendor of the invoice template.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoice templates by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoice templates by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoice templates to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceTemplateId]` — The ID of the invoice template to start after. If not provided, the first page of invoice templates will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoice templates by vendor name, check number, invoice number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoice templates by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoice templates by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoice templates by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoice templates by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoice templates by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoice templates by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoice templates by approver action. Needs to be used with approverId. For example, if you want to find all invoice templates that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoice templates by invoice ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoice templates by recurring status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import (
    InvoiceLineItemCreationRequest,
    InvoiceTemplateCreationRequest,
    PaymentDestinationOptions_Check,
    PaymentSchedule_Monthly,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.create(
    request=InvoiceTemplateCreationRequest(
        status="NEW",
        amount=100.0,
        currency="USD",
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-13 00:00:00+00:00",
        ),
        deduction_date=datetime.datetime.fromisoformat(
            "2021-01-10 00:00:00+00:00",
        ),
        payment_schedule=PaymentSchedule_Monthly(
            repeat_on_day=10,
            ends=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
        invoice_number="INV-123",
        note_to_self="Monthly recurring payment",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        payment_destination_options=PaymentDestinationOptions_Check(
            delivery="MAIL",
            print_description=True,
        ),
        line_items=[
            InvoiceLineItemCreationRequest(
                amount=100.0,
                currency="USD",
                description="Product A",
                name="Product A",
                quantity=1.0,
                unit_price=100.0,
                category="EXPENSE",
                service_start_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                service_end_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                metadata={"key1": "value1", "key2": "value2"},
                gl_account_id="600394",
            )
        ],
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InvoiceTemplateCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.get(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import (
    InvoiceLineItemUpdateRequest,
    InvoiceTemplateUpdateRequest,
    PaymentDestinationOptions_Check,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.update(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    request=InvoiceTemplateUpdateRequest(
        status="NEW",
        amount=100.0,
        currency="USD",
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        invoice_number="INV-123",
        note_to_self="For the month of January",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        payment_destination_options=PaymentDestinationOptions_Check(
            delivery="MAIL",
            print_description=True,
        ),
        line_items=[
            InvoiceLineItemUpdateRequest(
                id="inli_26672f38-eb9a-48f1-a7a0-f1b855e38cd7",
                amount=100.0,
                currency="USD",
                description="Product A",
                name="Product A",
                quantity=1.0,
                unit_price=100.0,
                category="EXPENSE",
                service_start_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                service_end_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                metadata={"key1": "value1", "key2": "value2"},
                gl_account_id="600394",
            )
        ],
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceTemplateUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only invoice templates in the UNASSIGNED and DRAFT statuses can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.delete(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InvoiceTemplate LineItem
<details><summary><code>client.invoice_template.line_item.<a href="src/mercoa/invoice_template/line_item/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update invoice template line item
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import InvoiceLineItemIndividualUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.line_item.update(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    line_item_id="inli_8aa84cb8-2ae7-4579-8fa3-87586e7c14a7",
    request=InvoiceLineItemIndividualUpdateRequest(
        name="Product A",
        description="Product A",
        service_start_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        service_end_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        metadata={"key1": "value1", "key2": "value2"},
        gl_account_id="600394",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `InvoiceLineItemId` — Invoice Line Item ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceLineItemIndividualUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice
<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search invoices for all entities in the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by the ID or foreign ID of the entity that is the payer or the vendor of the invoice.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoices by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID. Only invoices with all upstream policies approved will be returned.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by recurring status
    
</dd>
</dl>

<dl>
<dd>

**invoice_template_id:** `typing.Optional[
    typing.Union[InvoiceTemplateId, typing.Sequence[InvoiceTemplateId]]
]` — Filter invoice by invoice template ID
    
</dd>
</dl>

<dl>
<dd>

**return_payer_metadata:** `typing.Optional[bool]` — Whether to return payer metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_vendor_metadata:** `typing.Optional[bool]` — Whether to return vendor metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import InvoiceCreationWithEntityRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.create(
    request=InvoiceCreationWithEntityRequest(
        status="SCHEDULED",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        currency="USD",
        amount=100.0,
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        deduction_date=datetime.datetime.fromisoformat(
            "2021-01-29 00:00:00+00:00",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InvoiceCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.get(
    invoice_id="in_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import InvoiceUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.update(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    request=InvoiceUpdateRequest(
        vendor_credit_ids=["vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only invoices in the UNASSIGNED and DRAFT statuses can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.delete(
    invoice_id="in_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all events for an invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.events(
    invoice_id="in_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. If not provided, events from the start of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. If not provided, events to the end of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Limit can range between 1 and 100, and the default is 50.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceEventId]` — The ID of the event to start after. If not provided, the first page of events will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice LineItem
<details><summary><code>client.invoice.line_item.<a href="src/mercoa/invoice/line_item/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update invoice line item
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import InvoiceLineItemIndividualUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.line_item.update(
    invoice_id="in_d8f68285-1c6d-4d5a-a9e3-252c3180fac4",
    line_item_id="inli_8aa84cb8-2ae7-4579-8fa3-87586e7c14a7",
    request=InvoiceLineItemIndividualUpdateRequest(
        name="Product A",
        description="Product A",
        service_start_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        service_end_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        metadata={"key1": "value1", "key2": "value2"},
        gl_account_id="600394",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `InvoiceLineItemId` — Invoice Line Item ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceLineItemIndividualUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization
<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current organization information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — include supported payment methods in response
    
</dd>
</dl>

<dl>
<dd>

**email_provider:** `typing.Optional[bool]` — include email provider info in response
    
</dd>
</dl>

<dl>
<dd>

**external_accounting_system_provider:** `typing.Optional[bool]` — include external accounting system provider info in response
    
</dd>
</dl>

<dl>
<dd>

**color_scheme:** `typing.Optional[bool]` — include color scheme info in response
    
</dd>
</dl>

<dl>
<dd>

**payee_onboarding_options:** `typing.Optional[bool]` — include payee onboarding options in response
    
</dd>
</dl>

<dl>
<dd>

**payor_onboarding_options:** `typing.Optional[bool]` — include payor onboarding options in response
    
</dd>
</dl>

<dl>
<dd>

**metadata_schema:** `typing.Optional[bool]` — include metadata schema in response
    
</dd>
</dl>

<dl>
<dd>

**notification_email_template:** `typing.Optional[bool]` — include notification-email-template in response
    
</dd>
</dl>

<dl>
<dd>

**role_permissions:** `typing.Optional[bool]` — include role permission config in response
    
</dd>
</dl>

<dl>
<dd>

**custom_domains:** `typing.Optional[bool]` — include custom domains in response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update current organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.organization_types import OrganizationRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.update(
    request=OrganizationRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrganizationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">email_log</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get log of all emails sent to this organization. Content format subject to change.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.email_log()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Filter by sender email address
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` — Filter by recipient email address
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of logs to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — The ID of the log to start after. If not provided, the first page of logs will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">invalidate_tokens</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate all JWT tokens for the current organization. This is considered a break-glass action and should be used only if tokens have been compromised. All tokens will be invalidated, including tokens on links, emails, and currently logged in sessions. API keys are not affected by this action. This action may take 60 seconds to propagate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.invalidate_tokens()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `typing.Optional[typing.Sequence[str]]` — Optional list of session IDs to invalidate. If not provided, all sessions will be invalidated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BankLookup
<details><summary><code>client.bank_lookup.<a href="src/mercoa/bank_lookup/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find bank account details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.bank_lookup.find(
    routing_number="026009593",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**routing_number:** `str` — Routing number to validate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Calculate
<details><summary><code>client.calculate.<a href="src/mercoa/calculate/client.py">fee</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculate the estimated fees associated with an payment given the amount, payment source, and disbursement method. Can be used to calculate fees for a payment before creating an invoice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.calculate import CalculateFeesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.calculate.fee(
    request=CalculateFeesRequest(
        amount=100.0,
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CalculateFeesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calculate.<a href="src/mercoa/calculate/client.py">payment_timing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculate the estimated payment timing given the deduction date, payment source, and disbursement method. Can be used to calculate timing for a payment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.calculate import InvoiceTiming

client = Mercoa(
    token="YOUR_TOKEN",
)
client.calculate.payment_timing(
    request=InvoiceTiming(
        invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CalculatePaymentTimingRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomPaymentMethodSchema
<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">get_all</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all custom payment method schemas
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create custom payment method schema
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import (
    CustomPaymentMethodSchemaField,
    CustomPaymentMethodSchemaRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.create(
    request=CustomPaymentMethodSchemaRequest(
        name="Check",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="payToTheOrderOf",
                display_name="Pay To The Order Of",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="usBankAccountNumber",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="usBankRoutingNumber",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="address",
                display_name="Address",
                type="address",
                optional=False,
            ),
        ],
        estimated_processing_time=7,
        max_amount=50000.0,
        min_amount=1.0,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CustomPaymentMethodSchemaRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update custom payment method schema
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import (
    CustomPaymentMethodSchemaField,
    CustomPaymentMethodSchemaRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.update(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
    request=CustomPaymentMethodSchemaRequest(
        name="Wire",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD", "EUR"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="bankName",
                display_name="Bank Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="recipientName",
                display_name="Recipient Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="usBankAccountNumber",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="usBankRoutingNumber",
                optional=False,
            ),
        ],
        estimated_processing_time=0,
        max_amount=100000.0,
        min_amount=1.0,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `CustomPaymentMethodSchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CustomPaymentMethodSchemaRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get custom payment method schema
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.get(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `CustomPaymentMethodSchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete custom payment method schema. Schema that have been used in an invoice cannot be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.delete(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `CustomPaymentMethodSchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EntityGroup Invoice
<details><summary><code>client.entity_group.invoice.<a href="src/mercoa/entity_group/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoices for an entity group with the given filters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.invoice.find(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    exclude_receivables=True,
    order_by="CREATED_AT",
    order_direction="ASC",
    limit=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**exclude_payables:** `typing.Optional[bool]` — Return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date for invoice created on date filter.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date for invoice created date filter.
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on.
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by recurring status
    
</dd>
</dl>

<dl>
<dd>

**return_payer_metadata:** `typing.Optional[bool]` — Whether to return payer metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_vendor_metadata:** `typing.Optional[bool]` — Whether to return vendor metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.invoice.<a href="src/mercoa/entity_group/invoice/client.py">metrics</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoice metrics for an entity group with the given filters. Invoices will be grouped by currency. If none of excludePayables, excludeReceivables, payerId, vendorId, or invoiceId status filters are provided, excludeReceivables will be set to true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.invoice.metrics(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    return_by_date="CREATION_DATE",
    exclude_receivables=True,
    start_date=datetime.datetime.fromisoformat(
        "2021-01-01 00:00:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2021-01-31 23:59:59.999000+00:00",
    ),
    currency="USD",
    status="NEW",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**exclude_payables:** `typing.Optional[bool]` — Only return invoices that are not payable by the entity. This will return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Only return invoices that are not receivable by the entity. This will return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**return_by_date:** `typing.Optional[InvoiceMetricsPerDateGroupBy]` — Return invoice metrics grouped by date.
    
</dd>
</dl>

<dl>
<dd>

**return_by_date_frequency:** `typing.Optional[InvoiceMetricsPerDateFrequency]` — Return invoice metrics grouped by date. Defaults to daily.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[
    typing.Union[InvoiceMetricsGroupBy, typing.Sequence[InvoiceMetricsGroupBy]]
]` — Return invoice metrics grouped by.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[typing.Union[CurrencyCode, typing.Sequence[CurrencyCode]]]` — Currency to filter on
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity ApprovalPolicy
<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all invoice approval policies associated with an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.approval_policy.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an invoice approval policy associated with an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    ApprovalPolicyRequest,
    IdentifierList_UserList,
    Rule_Approver,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.approval_policy.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=ApprovalPolicyRequest(
        trigger=[],
        rule=Rule_Approver(
            num_approvers=2,
            identifier_list=IdentifierList_UserList(
                value=[
                    "usr_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                    "usr_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                ]
            ),
        ),
        upstream_policy_id="root",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApprovalPolicyRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an invoice approval policy associated with an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.approval_policy.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `ApprovalPolicyId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an invoice approval policy associated with an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    ApprovalPolicyUpdateRequest,
    IdentifierList_UserList,
    Rule_Approver,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.approval_policy.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
    request=ApprovalPolicyUpdateRequest(
        trigger=[],
        rule=Rule_Approver(
            num_approvers=2,
            identifier_list=IdentifierList_UserList(
                value=[
                    "usr_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                    "usr_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                ]
            ),
        ),
        upstream_policy_id="root",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `ApprovalPolicyId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApprovalPolicyUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an invoice approval policy associated with Entity. BEWARE: Any approval policy deletion will result in all associated downstream policies also being deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.approval_policy.delete(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `ApprovalPolicyId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Bulk
<details><summary><code>client.entity.bulk.<a href="src/mercoa/entity/bulk/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple entities in bulk. This endpoint will process synchronously and return a list of entities that were created or failed to create.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.commons import Address, PhoneNumber
from mercoa.entity_types import (
    BulkConnectedEntity,
    BulkEntityCreationFromObject,
    BusinessProfileRequest,
    Ein,
    EntityCreationRequest,
    ProfileRequest,
    TaxId,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.bulk.create(
    request=BulkEntityCreationFromObject(
        connected_entity=BulkConnectedEntity(
            id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
            link_created_as_payor=False,
            link_created_as_payee=True,
        ),
        entities=[
            EntityCreationRequest(
                is_customer=True,
                is_payor=True,
                is_payee=False,
                account_type="business",
                foreign_id="MY-DB-ID-12345",
                profile=ProfileRequest(
                    business=BusinessProfileRequest(
                        email="customer@acme.com",
                        legal_business_name="Acme Inc.",
                        website="http://www.acme.com",
                        business_type="llc",
                        phone=PhoneNumber(
                            country_code="1",
                            number="4155551234",
                        ),
                        address=Address(
                            address_line_1="123 Main St",
                            address_line_2="Unit 1",
                            city="San Francisco",
                            state_or_province="CA",
                            postal_code="94105",
                            country="US",
                        ),
                        tax_id=TaxId(
                            ein=Ein(
                                number="12-3456789",
                            ),
                        ),
                    ),
                ),
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BulkEntityCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**emit_webhooks:** `typing.Optional[bool]` — If true, webhooks will be emitted for each entity that is created. By default, webhooks are not emitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Counterparty VendorCredit
<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.vendor_credit.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.vendor_credit.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**vendor_credit_id:** `VendorCreditId` — ID of the vendor credit to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.vendor_credit_types import VendorCreditRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.vendor_credit.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    request=VendorCreditRequest(
        total_amount=100.0,
        currency="USD",
        note="This is a note",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `VendorCreditRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.vendor_credit.delete(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**vendor_credit_id:** `VendorCreditId` — ID of the vendor credit to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">estimate_usage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Estimate the usage of vendor credits on an invoice of a given amount
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.vendor_credit.estimate_usage(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    amount=150.0,
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — The amount of the invoice to calculate vendor credit usage for.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyCode]` — The currency of the invoice to calculate vendor credit usage for. Defaults to USD.
    
</dd>
</dl>

<dl>
<dd>

**excluded_invoice_ids:** `typing.Optional[typing.Sequence[InvoiceId]]` — List of invoice IDs to exclude from the calculation. If not provided or an empty list, no invoices will be excluded. This is useful for recalculating vendor credit usage on invoices that already have vendor credits applied.
    
</dd>
</dl>

<dl>
<dd>

**included_vendor_credit_ids:** `typing.Optional[typing.Sequence[VendorCreditId]]` — List of vendor credit IDs to include in the calculation. If not provided, all applicable vendor credits will be included, while an empty list will not include ANY vendor credits.  This is useful for recalculating vendor credit usage on invoices that have a fixed list of applied vendor credits (e.g. a SCHEDULED or PENDING invoice).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Customization
<details><summary><code>client.entity.customization.<a href="src/mercoa/entity/customization/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity customization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.customization.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.customization.<a href="src/mercoa/entity/customization/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity customization. This lets you turn off metadata and payment methods for an entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.customization_types import (
    FeeCustomizationDetailRequest,
    FeeCustomizationRailRequest,
    FeeCustomizationRequest,
    MetadataCustomizationRequest,
    NotificationCustomizationRequest,
    OcrCustomizationRequest,
    PaymentMethodCustomizationRequest_BankAccount,
    PaymentMethodCustomizationRequest_Check,
    PaymentMethodCustomizationRequest_Custom,
    PaymentMethodFee_Flat,
    PaymentMethodFee_Percentage,
    WorkflowCustomizationRequest,
)
from mercoa.entity_types import EntityCustomizationRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.customization.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityCustomizationRequest(
        metadata=[
            MetadataCustomizationRequest(
                key="my_custom_field",
                disabled=True,
            ),
            MetadataCustomizationRequest(
                key="my_other_field",
                disabled=False,
            ),
        ],
        payment_source=[
            PaymentMethodCustomizationRequest_BankAccount(
                disabled=True,
                default_delivery_method="ACH_SAME_DAY",
            ),
            PaymentMethodCustomizationRequest_Custom(
                schema_id="cpms_7df2974a-4069-454c-912f-7e58ebe030fb",
                disabled=True,
            ),
        ],
        backup_disbursement=[
            PaymentMethodCustomizationRequest_Check(
                disabled=True,
                default_delivery_method="MAIL",
                print_description=True,
            )
        ],
        payment_destination=[
            PaymentMethodCustomizationRequest_BankAccount(
                disabled=True,
                default_delivery_method="ACH_SAME_DAY",
            ),
            PaymentMethodCustomizationRequest_Check(
                disabled=True,
                default_delivery_method="MAIL",
                print_description=True,
            ),
        ],
        ocr=OcrCustomizationRequest(
            line_items=True,
            collapse_line_items=True,
            invoice_metadata=True,
            line_item_metadata=True,
            line_item_gl_account_id=True,
            predict_metadata=True,
            tax_and_shipping_as_line_items=True,
            split_documents=True,
        ),
        notifications=NotificationCustomizationRequest(
            assume_role="admin",
        ),
        workflow=WorkflowCustomizationRequest(
            auto_advance_invoice_status=True,
        ),
        role_permissions={"admin": ["invoice.all", "paymentMethod.all"]},
        fees=FeeCustomizationRequest(
            payable=FeeCustomizationDetailRequest(
                source=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                ),
                destination=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                ),
            ),
            receivable=FeeCustomizationDetailRequest(
                source=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                ),
                destination=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                ),
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityCustomizationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Document
<details><summary><code>client.entity.document.<a href="src/mercoa/entity/document/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get documents (1099/W9) associated with this entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.document.get_all(
    entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]]` — Filter by document type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.document.<a href="src/mercoa/entity/document/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload documents associated with this entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.document.upload(
    entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
    type="TEN_NINETY_NINE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` 
    
</dd>
</dl>

<dl>
<dd>

**document:** `str` — Base64 encoded image or PDF of document. PNG, JPG, WEBP, and PDF are supported. 10MB max.
    
</dd>
</dl>

<dl>
<dd>

**type:** `DocumentType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.document.<a href="src/mercoa/entity/document/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a document associated with this entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.document.delete(
    entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity EmailTemplate
<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all email templates for the entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_template.get_all(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EmailTemplateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_template.create(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EmailTemplateRequest(
        template_type="PAYMENT",
        name="Generic Payment Email",
        subject="Action Required - Your payment is due",
        content="<h1>Your invoice has been sent.</h1>",
        is_default=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EmailTemplateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity email template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_template.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    email_template_id="emt_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**email_template_id:** `EmailTemplateId` — Email Template ID or Email Template ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity email template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EmailTemplateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_template.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    email_template_id="emt_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EmailTemplateRequest(
        template_type="PAYMENT",
        name="Generic Payment Email",
        subject="Action Required - Your payment is due",
        content="<h1>Your invoice has been sent.</h1>",
        is_default=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**email_template_id:** `EmailTemplateId` — Email Template ID or Email Template ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EmailTemplateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity email template. This will also remove the email template from all entities.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_template.delete(
    entity_id="entityId",
    email_template_id="emailTemplateId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**email_template_id:** `EmailTemplateId` — Email Template ID or Email Template ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity ExternalAccountingSystem
<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the external accounting system connected to an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.external_accounting_system.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create/Link an entity to an external accounting system like Codat or Rutter. If the entity is already linked to an external accounting system, this will return the existing connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity.external_accounting_system import (
    ExternalAccountingSystemCompanyCreationRequest_Rutter,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.external_accounting_system.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=ExternalAccountingSystemCompanyCreationRequest_Rutter(
        access_token="123",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExternalAccountingSystemCompanyCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">connect</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a link to connect an entity to an external accounting system like Quickbooks or Xero
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.external_accounting_system.connect(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync an entity with an external accounting system. Will sync customers/vendors and invoices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.external_accounting_system.sync(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    vendors="pull",
    bills="push",
    gl_accounts="pull",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**vendors:** `typing.Optional[SyncType]` — Sync vendors from external accounting system. Default is to pull vendors from external system.
    
</dd>
</dl>

<dl>
<dd>

**bills:** `typing.Optional[SyncType]` — Sync bills from external accounting system. Default is to not sync bills. Invoices that already exist in both systems will not be updated, only new invoices not present in the other system will be created.
    
</dd>
</dl>

<dl>
<dd>

**gl_accounts:** `typing.Optional[SyncType]` — Sync GL accounts from external accounting system. Default is to pull GL accounts from external system. Pushing GL accounts is not supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Invoice
<details><summary><code>client.entity.invoice.<a href="src/mercoa/entity/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoices for an entity with the given filters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.invoice.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    exclude_receivables=True,
    order_by="CREATED_AT",
    order_direction="ASC",
    limit=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**exclude_payables:** `typing.Optional[bool]` — Return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoices by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on.
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by payment type.
    
</dd>
</dl>

<dl>
<dd>

**return_payer_metadata:** `typing.Optional[bool]` — Whether to return payer metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_vendor_metadata:** `typing.Optional[bool]` — Whether to return vendor metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_payment_timing:** `typing.Optional[bool]` — Whether to return payment timing in the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.invoice.<a href="src/mercoa/entity/invoice/client.py">metrics</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoice metrics for an entity with the given filters. Invoices will always be grouped by currency. If none of excludePayables, excludeReceivables, payerId, vendorId, or invoiceId status filters are provided, excludeReceivables will be set to true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.invoice.metrics(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    return_by_date="CREATION_DATE",
    exclude_receivables=True,
    start_date=datetime.datetime.fromisoformat(
        "2021-01-01 00:00:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2021-01-31 23:59:59.999000+00:00",
    ),
    currency="USD",
    status="NEW",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**exclude_payables:** `typing.Optional[bool]` — Only return invoices that are not payable by the entity. This will return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Only return invoices that are not receivable by the entity. This will return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**return_by_date:** `typing.Optional[InvoiceMetricsPerDateGroupBy]` — Return invoice metrics grouped by date.
    
</dd>
</dl>

<dl>
<dd>

**return_by_date_frequency:** `typing.Optional[InvoiceMetricsPerDateFrequency]` — Return invoice metrics grouped by date. Defaults to daily.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[
    typing.Union[InvoiceMetricsGroupBy, typing.Sequence[InvoiceMetricsGroupBy]]
]` — Return invoice metrics grouped by.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[typing.Union[CurrencyCode, typing.Sequence[CurrencyCode]]]` — Currency to filter on
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Metadata
<details><summary><code>client.entity.metadata.<a href="src/mercoa/entity/metadata/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all metadata options associated with this entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.metadata.get_all(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.metadata.<a href="src/mercoa/entity/metadata/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve metadata associated with a specific key
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.metadata.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    key="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.metadata.<a href="src/mercoa/entity/metadata/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update metadata associated with a specific key
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.metadata.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    key="glAccountId",
    request=[
        "{key: '60205', value: {value: '60205 Marketing Expense', subtitle: 'Expense'}}",
        "{key: '60215', value: {value: '60215 Office Expense', subtitle: 'Expense'}}",
        "{key: '60225', value: {value: '60225 Payroll Expense', subtitle: 'Expense'}}",
        "{key: '60550', value: {value: '60550 Rent Expense', subtitle: 'Expense'}}",
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.metadata.<a href="src/mercoa/entity/metadata/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all metadata associated with a specific key
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.metadata.delete(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    key="propertyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity NotificationPolicy
<details><summary><code>client.entity.notification_policy.<a href="src/mercoa/entity/notification_policy/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all notification policies associated with this entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.notification_policy.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.notification_policy.<a href="src/mercoa/entity/notification_policy/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve notification policy associated with this entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.notification_policy.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    notification_type="INVOICE_APPROVED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.notification_policy.<a href="src/mercoa/entity/notification_policy/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update notification policy associated with this entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import NotificationPolicyRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.notification_policy.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    notification_type="INVOICE_APPROVED",
    request=NotificationPolicyRequest(
        disabled=True,
        additional_roles=[],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NotificationPolicyRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity PaymentMethod BankAccount
<details><summary><code>client.entity.payment_method.bank_account.<a href="src/mercoa/entity/payment_method/bank_account/client.py">initiate_micro_deposits</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate micro deposits for a bank account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.bank_account.initiate_micro_deposits(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.bank_account.<a href="src/mercoa/entity/payment_method/bank_account/client.py">complete_micro_deposits</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Complete micro deposit verification
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.bank_account.complete_micro_deposits(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    amounts=[40, 2],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**amounts:** `typing.Sequence[int]` — The amounts of the micro deposits in cents
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity PaymentMethod Wallet
<details><summary><code>client.entity.payment_method.wallet.<a href="src/mercoa/entity/payment_method/wallet/client.py">get_wallet_balance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the available and pending balance of this entity's wallet. The specified payment method ID must refer to the entity's wallet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.wallet.get_wallet_balance(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.wallet.<a href="src/mercoa/entity/payment_method/wallet/client.py">add_wallet_funds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add funds to this wallet from a bank account (this transfer is D+2). The source payment method ID must refer to a bank account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.wallet.add_wallet_funds(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    amount=100.0,
    currency="USD",
    source_payment_method_id="pm_f19d27ad-e493-4bf5-a28b-9cb323de495a",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — The amount of the funds to add. If the entered amount has more decimal places than the currency supports, trailing decimals will be truncated.
    
</dd>
</dl>

<dl>
<dd>

**source_payment_method_id:** `PaymentMethodId` — The ID of the bank account to add funds from. The source payment method ID must refer to a bank account.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyCode]` — The currency of the funds to add. (Defaults to USD, currently only USD is supported.)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.wallet.<a href="src/mercoa/entity/payment_method/wallet/client.py">withdraw_wallet_funds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Withdraw funds from this wallet to a bank account (this transfer is D+0). The destination payment method ID must refer to a bank account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.wallet.withdraw_wallet_funds(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    amount=100.0,
    currency="USD",
    destination_payment_method_id="pm_f19d27ad-e493-4bf5-a28b-9cb323de495a",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — The amount of the funds to withdraw. If the entered amount has more decimal places than the currency supports, trailing decimals will be truncated.
    
</dd>
</dl>

<dl>
<dd>

**destination_payment_method_id:** `PaymentMethodId` — The ID of the bank account to withdraw funds to. The destination payment method ID must refer to a bank account.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyCode]` — The currency of the funds to withdraw. (Defaults to USD, currently only USD is supported.)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Representative
<details><summary><code>client.entity.representative.<a href="src/mercoa/entity/representative/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get representatives for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.representative.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.representative.<a href="src/mercoa/entity/representative/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.commons import (
    Address,
    BirthDate,
    FullName,
    IndividualGovernmentId,
    PhoneNumber,
)
from mercoa.entity_types import RepresentativeRequest, Responsibilities

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.representative.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=RepresentativeRequest(
        name=FullName(
            first_name="John",
            middle_name="Quincy",
            last_name="Adams",
            suffix="Jr.",
        ),
        phone=PhoneNumber(
            country_code="1",
            number="4155551234",
        ),
        email="john.doe@acme.com",
        address=Address(
            address_line_1="123 Main St",
            address_line_2="Unit 1",
            city="San Francisco",
            state_or_province="CA",
            postal_code="94105",
            country="US",
        ),
        birth_date=BirthDate(
            day="1",
            month="1",
            year="1980",
        ),
        government_id=IndividualGovernmentId(
            ssn="123-45-6789",
        ),
        responsibilities=Responsibilities(
            is_owner=True,
            ownership_percentage=40,
            is_controller=True,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `RepresentativeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.representative.<a href="src/mercoa/entity/representative/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.representative.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    representative_id="rep_7df2974a-4069-454c-912f-7e58ebe030fb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**representative_id:** `RepresentativeId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.representative.<a href="src/mercoa/entity/representative/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.commons import (
    Address,
    BirthDate,
    FullName,
    IndividualGovernmentId,
    PhoneNumber,
)
from mercoa.entity_types import RepresentativeUpdateRequest, Responsibilities

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.representative.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    representative_id="rep_7df2974a-4069-454c-912f-7e58ebe030fb",
    request=RepresentativeUpdateRequest(
        name=FullName(
            first_name="John",
            middle_name="Quincy",
            last_name="Adams",
            suffix="Jr.",
        ),
        phone=PhoneNumber(
            country_code="1",
            number="4155551234",
        ),
        email="john.doe@acme.com",
        address=Address(
            address_line_1="123 Main St",
            address_line_2="Unit 1",
            city="San Francisco",
            state_or_province="CA",
            postal_code="94105",
            country="US",
        ),
        birth_date=BirthDate(
            day="1",
            month="1",
            year="1980",
        ),
        government_id=IndividualGovernmentId(
            ssn="123-45-6789",
        ),
        responsibilities=Responsibilities(
            is_owner=True,
            ownership_percentage=40,
            is_controller=True,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**representative_id:** `RepresentativeId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RepresentativeUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.representative.<a href="src/mercoa/entity/representative/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.representative.delete(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    representative_id="rep_7df2974a-4069-454c-912f-7e58ebe030fb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**representative_id:** `RepresentativeId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity User NotificationPolicy
<details><summary><code>client.entity.user.notification_policy.<a href="src/mercoa/entity/user/notification_policy/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all notification policies associated with this entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.notification_policy.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.notification_policy.<a href="src/mercoa/entity/user/notification_policy/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve notification policy associated with this entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.notification_policy.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    notification_type="INVOICE_PAID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.notification_policy.<a href="src/mercoa/entity/user/notification_policy/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update notification policy associated with this entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import UserNotificationPolicyRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.notification_policy.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    notification_type="INVOICE_PAID",
    request=UserNotificationPolicyRequest(
        immediate=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UserNotificationPolicyRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity User Notifications
<details><summary><code>client.entity.user.notifications.<a href="src/mercoa/entity/user/notifications/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.notifications.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date for notification created on date filter.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date for notification created date filter.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order notifications by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[NotificationId]` — The ID of the notification to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**notification_type:** `typing.Optional[
    typing.Union[NotificationType, typing.Sequence[NotificationType]]
]` — The type of notification to filter by.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[NotificationStatus]` — The status of the notification to filter by.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.notifications.<a href="src/mercoa/entity/user/notifications/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.notifications.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    notification_id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**notification_id:** `NotificationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.notifications.<a href="src/mercoa/entity/user/notifications/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status of a notification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import NotificationUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.notifications.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    notification_id="notif_7df2974a-4069-454c-912f-7e58ebe030fb",
    request=NotificationUpdateRequest(
        status="READ",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**notification_id:** `NotificationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NotificationUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InvoiceTemplate Approval
<details><summary><code>client.invoice_template.approval.<a href="src/mercoa/invoice_template/approval/client.py">add_approver</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an approver to the invoice template. Will select the first available approver slot that is not already filled and assign the approver to it. If no approver slots are available, an error will be returned. An explicit approver slot can be specified by setting the `approverSlot` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import AddApproverRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.approval.add_approver(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    request=AddApproverRequest(
        approval_slot_id="inap_9bb311c9-7c15-4c9e-8148-63814e0abec6",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddApproverRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.approval.<a href="src/mercoa/invoice_template/approval/client.py">approve</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import ApprovalRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.approval.approve(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    request=ApprovalRequest(
        text="This is a reason for my action",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApprovalRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.approval.<a href="src/mercoa/invoice_template/approval/client.py">reject</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import ApprovalRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.approval.reject(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    request=ApprovalRequest(
        text="This is a reason for my action",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApprovalRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InvoiceTemplate Document
<details><summary><code>client.invoice_template.document.<a href="src/mercoa/invoice_template/document/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get attachments (scanned/uploaded PDFs and images) associated with this invoice template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.document.get_all(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]]` — Filter by document type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.document.<a href="src/mercoa/invoice_template/document/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload documents (scanned/uploaded PDFs and images) associated with this invoice template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.document.upload(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**document:** `str` — Base64-encoded string. Supported file types include PNG, JPG, WEBP, PDF, and all Microsoft Office formats (automatically converted to PDF). Max file size 10MB.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[DocumentType]` — Specify Document Type, defaults to INVOICE
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.document.<a href="src/mercoa/invoice_template/document/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an attachment (scanned/uploaded PDFs and images) associated with this invoice template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.document.delete(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.document.<a href="src/mercoa/invoice_template/document/client.py">generate_invoice_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a PDF of the invoice. This PDF is generated from the data in the invoice, not from the uploaded documents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.document.generate_invoice_pdf(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.document.<a href="src/mercoa/invoice_template/document/client.py">generate_check_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a PDF of the check for the invoice. If the invoice does not have check as the disbursement method, an error will be returned. If the disbursement option for the check is set to 'MAIL', a void copy of the check will be returned. If the disbursement option for the check is set to 'PRINT', a printable check will be returned. If the invoice is NOT marked as PAID, the check will be a void copy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.document.generate_check_pdf(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.document.<a href="src/mercoa/invoice_template/document/client.py">get_source_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the email subject and body that was used to create this invoice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.document.get_source_email(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice Approval
<details><summary><code>client.invoice.approval.<a href="src/mercoa/invoice/approval/client.py">add_approver</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an approver to the invoice. Will select the first available approver slot that is not already filled and assign the approver to it. If no approver slots are available, an error will be returned. An explicit approver slot can be specified by setting the `approverSlot` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import AddApproverRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.approval.add_approver(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    request=AddApproverRequest(
        approval_slot_id="inap_9bb311c9-7c15-4c9e-8148-63814e0abec6",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddApproverRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.approval.<a href="src/mercoa/invoice/approval/client.py">approve</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import ApprovalRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.approval.approve(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    request=ApprovalRequest(
        text="This is a reason for my action",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApprovalRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.approval.<a href="src/mercoa/invoice/approval/client.py">reject</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import ApprovalRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.approval.reject(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    request=ApprovalRequest(
        text="This is a reason for my action",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApprovalRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice Bulk
<details><summary><code>client.invoice.bulk.<a href="src/mercoa/invoice/bulk/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple invoices in bulk. This endpoint will process synchronously and return a list of invoices that were created or failed to create.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import (
    BulkInvoiceCreationRequest,
    InvoiceCreationWithEntityRequest,
    InvoiceLineItemCreationRequest,
    PaymentDestinationOptions_Check,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.bulk.create(
    request=BulkInvoiceCreationRequest(
        invoices=[
            InvoiceCreationWithEntityRequest(
                status="NEW",
                amount=100.0,
                currency="USD",
                invoice_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                due_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                invoice_number="INV-123",
                note_to_self="For the month of January",
                payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
                vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
                payment_destination_options=PaymentDestinationOptions_Check(
                    delivery="MAIL",
                    print_description=True,
                ),
                line_items=[
                    InvoiceLineItemCreationRequest(
                        amount=100.0,
                        currency="USD",
                        description="Product A",
                        name="Product A",
                        quantity=1.0,
                        unit_price=100.0,
                        category="EXPENSE",
                        service_start_date=datetime.datetime.fromisoformat(
                            "2021-01-01 00:00:00+00:00",
                        ),
                        service_end_date=datetime.datetime.fromisoformat(
                            "2021-01-31 00:00:00+00:00",
                        ),
                        metadata={"key1": "value1", "key2": "value2"},
                        gl_account_id="600394",
                    )
                ],
                creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
                creator_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BulkInvoiceCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**emit_webhooks:** `typing.Optional[bool]` — If true, webhooks will be emitted for each invoice that is created. By default, webhooks are not emitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.bulk.<a href="src/mercoa/invoice/bulk/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update multiple invoices in bulk. This endpoint will process synchronously and return a list of invoices that were updated or failed to update.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import (
    BulkInvoiceUpdateRequest,
    InvoiceLineItemUpdateRequest,
    InvoiceUpdateRequestWithId,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.bulk.update(
    request=BulkInvoiceUpdateRequest(
        invoices=[
            InvoiceUpdateRequestWithId(
                invoice_id="inv_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                status="NEW",
                amount=100.0,
                currency="USD",
                due_date=datetime.datetime.fromisoformat(
                    "2024-01-31 00:00:00+00:00",
                ),
                invoice_date=datetime.datetime.fromisoformat(
                    "2024-01-01 00:00:00+00:00",
                ),
                invoice_number="INV-001",
                line_items=[
                    InvoiceLineItemUpdateRequest(
                        description="Item 1",
                        amount=50.0,
                        quantity=1.0,
                    ),
                    InvoiceLineItemUpdateRequest(
                        description="Item 2",
                        amount=50.0,
                        quantity=1.0,
                    ),
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BulkInvoiceUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**emit_webhooks:** `typing.Optional[bool]` — If true, webhooks will be emitted for each invoice that is updated. By default, webhooks are not emitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.bulk.<a href="src/mercoa/invoice/bulk/client.py">approve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve multiple invoices in bulk. This endpoint will process synchronously and return a list of invoices that were approved or failed to approve.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import (
    ApprovalRequestWithId,
    BulkInvoiceApprovalRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.bulk.approve(
    request=BulkInvoiceApprovalRequest(
        invoices=[
            ApprovalRequestWithId(
                invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
                text="This is a reason for my action",
                user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BulkInvoiceApprovalRequest` 
    
</dd>
</dl>

<dl>
<dd>

**emit_webhooks:** `typing.Optional[bool]` — If true, webhooks will be emitted for each invoice that is approved. By default, webhooks are not emitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice Collection
<details><summary><code>client.invoice.collection.<a href="src/mercoa/invoice/collection/client.py">get_next_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the collection agent's next action on this invoice. This endpoint will return an empty object if there is no action to return.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.collection.get_next_action(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.collection.<a href="src/mercoa/invoice/collection/client.py">update_next_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the collection agent's next action on this invoice with natural language. Note that updating any APPROVED action will reset the action to SUGGESTED.  This endpoint will throw an error if there is no action to update.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.collection_types import UpdateNextActionRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.collection.update_next_action(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    request=UpdateNextActionRequest(
        feedback="Use a more stern tone",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateNextActionRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.collection.<a href="src/mercoa/invoice/collection/client.py">approve_next_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve the collection agent's next action on this invoice. This endpoint will throw an error if there is no action to approve.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.collection.approve_next_action(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice Comment
<details><summary><code>client.invoice.comment.<a href="src/mercoa/invoice/comment/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all comments associated with this invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.comment.get_all(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.comment.<a href="src/mercoa/invoice/comment/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a comment to this invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import CommentRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.comment.create(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    request=CommentRequest(
        text="This is a comment",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `CommentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.comment.<a href="src/mercoa/invoice/comment/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.comment.get(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**comment_id:** `CommentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.comment.<a href="src/mercoa/invoice/comment/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit a comment on this invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import CommentRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.comment.update(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    request=CommentRequest(
        text="This is a comment",
        user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**comment_id:** `CommentId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CommentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.comment.<a href="src/mercoa/invoice/comment/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a comment on this invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.comment.delete(
    invoice_id="in_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
    comment_id="ic_3d61faa9-1754-4b7b-9fcb-88ff97f368ff",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**comment_id:** `CommentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice Document
<details><summary><code>client.invoice.document.<a href="src/mercoa/invoice/document/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get attachments (scanned/uploaded PDFs and images) associated with this invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.document.get_all(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]]` — Filter by document type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.document.<a href="src/mercoa/invoice/document/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload documents (scanned/uploaded PDFs and images) associated with this Invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.document.upload(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**document:** `str` — Base64-encoded string. Supported file types include PNG, JPG, WEBP, PDF, and all Microsoft Office formats (automatically converted to PDF). Max file size 10MB.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[DocumentType]` — Specify Document Type, defaults to INVOICE
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.document.<a href="src/mercoa/invoice/document/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an attachment (scanned/uploaded PDFs and images) associated with this invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.document.delete(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.document.<a href="src/mercoa/invoice/document/client.py">generate_invoice_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a PDF of the invoice. This PDF is generated from the data in the invoice, not from the uploaded documents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.document.generate_invoice_pdf(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.document.<a href="src/mercoa/invoice/document/client.py">generate_check_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a PDF of the check for the invoice. If the invoice does not have check as the disbursement method, an error will be returned. If the disbursement option for the check is set to 'MAIL', a void copy of the check will be returned. If the disbursement option for the check is set to 'PRINT', a printable check will be returned. If the invoice is NOT marked as PAID, the check will be a void copy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.document.generate_check_pdf(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.document.<a href="src/mercoa/invoice/document/client.py">get_source_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the email subject and body that was used to create this invoice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.document.get_source_email(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice PaymentLinks
<details><summary><code>client.invoice.payment_links.<a href="src/mercoa/invoice/payment_links/client.py">get_payer_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get temporary link for payer to send payment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.payment_links.get_payer_link(
    invoice_id="in_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 30d.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.payment_links.<a href="src/mercoa/invoice/payment_links/client.py">send_payer_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger email to payer inviting them to make payment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.payment_links.send_payer_email(
    invoice_id="in_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    attach_invoice=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**attach_invoice:** `typing.Optional[bool]` — Whether to attach the invoice to the email
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.payment_links.<a href="src/mercoa/invoice/payment_links/client.py">get_vendor_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get temporary link for vendor to accept payment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.payment_links.get_vendor_link(
    invoice_id="in_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 30d.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice.payment_links.<a href="src/mercoa/invoice/payment_links/client.py">send_vendor_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger email to vendor inviting them into the vendor portal
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.payment_links.send_vendor_email(
    invoice_id="in_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ocr
<details><summary><code>client.ocr.<a href="src/mercoa/ocr/client.py">ocr</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run OCR on an Base64 encoded image or PDF. This endpoint will block until the OCR is complete.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.ocr import OcrRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.ocr.ocr(
    request=OcrRequest(
        vendor_network="entity",
        entity_id="ent_8f86116b-3b4d-4ded-99ef-3bc929d8c33c",
        mime_type="image/png",
        image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OcrRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ocr.<a href="src/mercoa/ocr/client.py">run_async_ocr</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run OCR on an Base64 encoded image or PDF. This endpoint will return immediately and the OCR will be processed asynchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.ocr import OcrRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.ocr.run_async_ocr(
    request=OcrRequest(
        vendor_network="entity",
        entity_id="ent_8f86116b-3b4d-4ded-99ef-3bc929d8c33c",
        mime_type="image/png",
        image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OcrRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ocr.<a href="src/mercoa/ocr/client.py">get_async_ocr</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status and results of an asynchronous OCR job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.ocr.get_async_ocr(
    job_id="ocr_8f86116b-3b4d-4ded-99ef-3bc929d8c33c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization NotificationConfiguration
<details><summary><code>client.organization.notification_configuration.<a href="src/mercoa/organization/notification_configuration/client.py">get_all</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all notification configurations
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.notification_configuration.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.notification_configuration.<a href="src/mercoa/organization/notification_configuration/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve notification configuration for this notification type
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.notification_configuration.get(
    notification_type="INVOICE_APPROVAL_NEEDED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.notification_configuration.<a href="src/mercoa/organization/notification_configuration/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update notification configuration for this notification type
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.organization_types import NotificationConfigurationRequest_Invoice

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.notification_configuration.update(
    notification_type="INVOICE_APPROVAL_NEEDED",
    request=NotificationConfigurationRequest_Invoice(
        url="url",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NotificationConfigurationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.notification_configuration.<a href="src/mercoa/organization/notification_configuration/client.py">reset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset notification configuration for this notification type
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.notification_configuration.reset(
    notification_type="INVOICE_APPROVAL_NEEDED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PaymentMethods
<details><summary><code>client.payment_methods.<a href="src/mercoa/payment_methods/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.payment_methods.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of payment methods to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[PaymentMethodId]` — The ID of the payment method to start after. If not provided, the first page of payment methods will be returned.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[
    typing.Union[PaymentMethodType, typing.Sequence[PaymentMethodType]]
]` — Type of payment method to filter
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Entity ID to filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transaction
<details><summary><code>client.transaction.<a href="src/mercoa/transaction/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search transactions
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.transaction.find(
    start_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    limit=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter transactions by the ID or foreign ID of the entity that created the transaction.
    
</dd>
</dl>

<dl>
<dd>

**entity_group_id:** `typing.Optional[EntityGroupId]` — Filter transactions by the ID or foreign ID of the entity group that the entity belongs to.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — CREATED_AT Start date filter.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — CREATED_AT End date filter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of transactions to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[TransactionId]` — The ID of the transactions to start after. If not provided, the first page of transactions will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find transactions by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter transactions by invoice metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter transactions by invoice line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter transactions by invoice line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter transactions by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter transactions by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter transactions by the ID or foreign ID of the user that created the invoice that created the transaction.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter transactions by invoice ID. Does not support foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[typing.Union[TransactionId, typing.Sequence[TransactionId]]]` — Filter transactions by transaction ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[
    typing.Union[TransactionStatus, typing.Sequence[TransactionStatus]]
]` — Transaction status to filter on
    
</dd>
</dl>

<dl>
<dd>

**transaction_type:** `typing.Optional[typing.Union[TransactionType, typing.Sequence[TransactionType]]]` — Filter transactions by transaction type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transaction.<a href="src/mercoa/transaction/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Transaction
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.transaction.get(
    transaction_id="trx_bb08e72f-19f8-45f3-bcf9-46fdc46cb2f4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transaction_id:** `TransactionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>


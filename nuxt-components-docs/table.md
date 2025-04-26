<!-- source: https://ui.nuxt.com/components/table --> # Table

[![TanStack Table avatar](https://github.com/tanstack.png)TanStack
Table](https://tanstack.com/table/latest)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Table.vue)

A responsive table element to display data in rows and columns.

## Usage

The Table component is built on top of [TanStack
Table](https://tanstack.com/table/latest) and is powered by the
[useVueTable](https://tanstack.com/table/latest/docs/framework/vue/vue-
table#usevuetable) composable to provide a flexible and fully type-safe API.
_Some features of TanStack Table are not supported yet, we'll add more over
time._

RandomizeColumns

| #| Date| Status| Email| Amount|  
---|---|---|---|---|---|---  
| #4600| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-
protection)| €594.00|  
| #4599| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €276.00|  
| #4598| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €315.00|  
| #4597| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-
protection)| €529.00|  
| #4596| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-
protection)| €639.00|  
| #4595| Mar 10, 13:40| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €428.00|  
| #4594| Mar 10, 09:15| paid| [[email protected]](/cdn-cgi/l/email-
protection)| €683.00|  
| #4593| Mar 9, 20:25| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €947.00|  
| #4592| Mar 9, 18:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€851.00|  
| #4591| Mar 9, 16:05| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€762.00|  
| #4590| Mar 9, 14:20| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€573.00|  
| #4589| Mar 9, 11:35| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €389.00|  
| #4588| Mar 8, 22:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €701.00|  
| #4587| Mar 8, 20:15| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€856.00|  
| #4586| Mar 8, 17:40| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€492.00|  
| #4585| Mar 8, 14:55| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €637.00|  
| #4584| Mar 8, 12:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€784.00|  
| #4583| Mar 8, 09:45| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €345.00|  
| #4582| Mar 7, 23:10| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€918.00|  
| #4581| Mar 7, 20:25| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€567.00|  
  
0 of 0 row(s) selected.

[](https://github.com/nuxt/ui/tree/v3/docs/app/components/content/examples/table/TableExample.vue)This
example demonstrates the most common use case of the `Table` component. Check
out the source code on GitHub.

### Data

Use the `data` prop as an array of objects, the columns will be generated
based on the keys of the objects.

Id| Date| Status| Email| Amount  
---|---|---|---|---  
4600| 2024-03-11T15:30:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 594  
4599| 2024-03-11T10:10:00| failed| [[email protected]](/cdn-cgi/l/email-
protection)| 276  
4598| 2024-03-11T08:50:00| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| 315  
4597| 2024-03-10T19:45:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 529  
4596| 2024-03-10T15:55:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 639  
      
    
    <script setup lang="ts">
    const data = ref([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    </script>
    
    <template>
      <UTable :data="data" class="flex-1" />
    </template>
    

Expand code

### Columns

Use the `columns` prop as an array of
[ColumnDef](https://tanstack.com/table/latest/docs/api/core/column-def)
objects with properties like:

  * `accessorKey`: The key of the row object to use when extracting the value for the column.
  * `header`: The header to display for the column. If a string is passed, it can be used as a default for the column ID. If a function is passed, it will be passed a props object for the header and should return the rendered header value (the exact type depends on the adapter being used).
  * `cell`: The cell to display each row for the column. If a function is passed, it will be passed a props object for the cell and should return the rendered cell value (the exact type depends on the adapter being used).
  * `meta`: Extra properties for the column.
    * `class`: 
      * `td`: The classes to apply to the `td` element.
      * `th`: The classes to apply to the `th` element.

In order to render components or other HTML elements, you will need to use the
Vue [`h` function](https://vuejs.org/api/render-function.html#h) inside the
`header` and `cell` props. This is different from other components that use
slots but allows for more flexibility.

You can also use slots to customize the header and data cells of the table.

#| Date| Status| Email| Amount  
---|---|---|---|---  
#4600| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
#4599| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €276.00  
#4598| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €315.00  
#4597| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
#4596| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    
    const UBadge = resolveComponent('UBadge')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    </script>
    
    <template>
      <UTable :data="data" :columns="columns" class="flex-1" />
    </template>
    

Expand code

When rendering components with `h`, you can either use the `resolveComponent`
function or import from `#components`.

### Meta

Use the `meta` prop as an object
([TableMeta](https://tanstack.com/table/latest/docs/api/core/table#meta)) to
pass properties like:

  * `class`: 
    * `tr`: The classes to apply to the `tr` element.

### Loading

Use the `loading` prop to display a loading state, the `loading-color` prop to
change its color and the `loading-animation` prop to change its animation.

loading

true

loadingColor

primary

loadingAnimation

carousel

Id| Date| Status| Email| Amount  
---|---|---|---|---  
4600| 2024-03-11T15:30:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 594  
4599| 2024-03-11T10:10:00| failed| [[email protected]](/cdn-cgi/l/email-
protection)| 276  
4598| 2024-03-11T08:50:00| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| 315  
4597| 2024-03-10T19:45:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 529  
4596| 2024-03-10T15:55:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 639  
      
    
    <script setup lang="ts">
    const data = ref([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    </script>
    
    <template>
      <UTable loading loading-color="primary" loading-animation="carousel" :data="data" class="flex-1" />
    </template>
    

Expand code

### Sticky

Use the `sticky` prop to make the header sticky.

sticky

true

Id| Date| Status| Email| Amount  
---|---|---|---|---  
4600| 2024-03-11T15:30:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 594  
4599| 2024-03-11T10:10:00| failed| [[email protected]](/cdn-cgi/l/email-
protection)| 276  
4598| 2024-03-11T08:50:00| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| 315  
4597| 2024-03-10T19:45:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 529  
4596| 2024-03-10T15:55:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 639  
4595| 2024-03-10T15:55:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 639  
4594| 2024-03-10T15:55:00| paid| [[email protected]](/cdn-cgi/l/email-
protection)| 639  
      
    
    <script setup lang="ts">
    const data = ref([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      },
      {
        id: '4595',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      },
      {
        id: '4594',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    </script>
    
    <template>
      <UTable sticky :data="data" class="flex-1 max-h-[312px]" />
    </template>
    

Expand code

## Examples

### With row actions

You can add a new column that renders a [DropdownMenu](/components/dropdown-
menu) component inside the `cell` to render row actions.

#| Date| Status| Email| Amount|  
---|---|---|---|---|---  
#4600| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00|  
#4599| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €276.00|  
#4598| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €315.00|  
#4597| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00|  
#4596| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00|  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    import type { Row } from '@tanstack/vue-table'
    
    const UButton = resolveComponent('UButton')
    const UBadge = resolveComponent('UBadge')
    const UDropdownMenu = resolveComponent('UDropdownMenu')
    
    const toast = useToast()
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      },
      {
        id: 'actions',
        cell: ({ row }) => {
          return h(
            'div',
            { class: 'text-right' },
            h(
              UDropdownMenu,
              {
                content: {
                  align: 'end'
                },
                items: getRowItems(row),
                'aria-label': 'Actions dropdown'
              },
              () =>
                h(UButton, {
                  icon: 'i-lucide-ellipsis-vertical',
                  color: 'neutral',
                  variant: 'ghost',
                  class: 'ml-auto',
                  'aria-label': 'Actions dropdown'
                })
            )
          )
        }
      }
    ]
    
    function getRowItems(row: Row<Payment>) {
      return [
        {
          type: 'label',
          label: 'Actions'
        },
        {
          label: 'Copy payment ID',
          onSelect() {
            navigator.clipboard.writeText(row.original.id)
    
            toast.add({
              title: 'Payment ID copied to clipboard!',
              color: 'success',
              icon: 'i-lucide-circle-check'
            })
          }
        },
        {
          type: 'separator'
        },
        {
          label: 'View customer'
        },
        {
          label: 'View payment details'
        }
      ]
    }
    </script>
    
    <template>
      <UTable :data="data" :columns="columns" class="flex-1" />
    </template>
    

Expand code

### With expandable rows

You can add a new column that renders a [Button](/components/button) component
inside the `cell` to toggle the expandable state of a row using the TanStack
Table [Expanding
APIs](https://tanstack.com/table/latest/docs/api/features/expanding).

You need to define the `#expanded` slot to render the expanded content which
will receive the row as a parameter.

| #| Date| Status| Email| Amount  
---|---|---|---|---|---  
| #4600| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-
protection)| €594.00  
| #4599| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €276.00  
      
    
    {
      "id": "4599",
      "date": "2024-03-11T10:10:00",
      "status": "failed",
      "email": "[[email protected]](/cdn-cgi/l/email-protection)",
      "amount": 276
    }  
  
| #4598| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €315.00  
| #4597| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-
protection)| €529.00  
| #4596| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-
protection)| €639.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    
    const UButton = resolveComponent('UButton')
    const UBadge = resolveComponent('UBadge')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        id: 'expand',
        cell: ({ row }) =>
          h(UButton, {
            color: 'neutral',
            variant: 'ghost',
            icon: 'i-lucide-chevron-down',
            square: true,
            'aria-label': 'Expand',
            ui: {
              leadingIcon: [
                'transition-transform',
                row.getIsExpanded() ? 'duration-200 rotate-180' : ''
              ]
            },
            onClick: () => row.toggleExpanded()
          })
      },
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const expanded = ref({ 1: true })
    </script>
    
    <template>
      <UTable
        v-model:expanded="expanded"
        :data="data"
        :columns="columns"
        :ui="{ tr: 'data-[expanded=true]:bg-elevated/50' }"
        class="flex-1"
      >
        <template #expanded="{ row }">
          <pre>{{ row.original }}</pre>
        </template>
      </UTable>
    </template>
    

Expand code

You can use the `expanded` prop to control the expandable state of the rows
(can be binded with `v-model`).

You could also add this action to the [`DropdownMenu`](/components/dropdown-
menu) component inside the `actions` column.

### With row selection

You can add a new column that renders a [Checkbox](/components/checkbox)
component inside the `header` and `cell` to select rows using the TanStack
Table [Row Selection
APIs](https://tanstack.com/table/latest/docs/api/features/row-selection).

| Date| Status| Email| Amount  
---|---|---|---|---  
| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-protection)|
€276.00  
| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-protection)|
€315.00  
| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00  
  
0 of 0 row(s) selected.

    
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    
    const UCheckbox = resolveComponent('UCheckbox')
    const UBadge = resolveComponent('UBadge')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        id: 'select',
        header: ({ table }) =>
          h(UCheckbox, {
            modelValue: table.getIsSomePageRowsSelected()
              ? 'indeterminate'
              : table.getIsAllPageRowsSelected(),
            'onUpdate:modelValue': (value: boolean | 'indeterminate') =>
              table.toggleAllPageRowsSelected(!!value),
            'aria-label': 'Select all'
          }),
        cell: ({ row }) =>
          h(UCheckbox, {
            modelValue: row.getIsSelected(),
            'onUpdate:modelValue': (value: boolean | 'indeterminate') => row.toggleSelected(!!value),
            'aria-label': 'Select row'
          })
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const table = useTemplateRef('table')
    
    const rowSelection = ref({ 1: true })
    </script>
    
    <template>
      <div class="flex-1 w-full">
        <UTable ref="table" v-model:row-selection="rowSelection" :data="data" :columns="columns" />
    
        <div class="px-4 py-3.5 border-t border-accented text-sm text-muted">
          {{ table?.tableApi?.getFilteredSelectedRowModel().rows.length || 0 }} of
          {{ table?.tableApi?.getFilteredRowModel().rows.length || 0 }} row(s) selected.
        </div>
      </div>
    </template>
    

Expand code

You can use the `row-selection` prop to control the selection state of the
rows (can be binded with `v-model`).

### With `@select` event

You can add a `@select` listener to make rows clickable. The handler function
receives the `TableRow` instance as the first argument and an optional `Event`
as the second argument.

You can use this to navigate to a page, open a modal or even to select the row
manually.

| Date| Status| Email| Amount  
---|---|---|---|---  
| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-protection)|
€276.00  
| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-protection)|
€315.00  
| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00  
  
0 of 0 row(s) selected.

    
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn, TableRow } from '@nuxt/ui'
    
    const UBadge = resolveComponent('UBadge')
    const UCheckbox = resolveComponent('UCheckbox')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        id: 'select',
        header: ({ table }) =>
          h(UCheckbox, {
            modelValue: table.getIsSomePageRowsSelected()
              ? 'indeterminate'
              : table.getIsAllPageRowsSelected(),
            'onUpdate:modelValue': (value: boolean | 'indeterminate') =>
              table.toggleAllPageRowsSelected(!!value),
            'aria-label': 'Select all'
          }),
        cell: ({ row }) =>
          h(UCheckbox, {
            modelValue: row.getIsSelected(),
            'onUpdate:modelValue': (value: boolean | 'indeterminate') => row.toggleSelected(!!value),
            'aria-label': 'Select row'
          })
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const table = useTemplateRef('table')
    
    const rowSelection = ref<Record<string, boolean>>({})
    
    function onSelect(row: TableRow<Payment>, e?: Event) {
      /* If you decide to also select the column you can do this  */
      row.toggleSelected(!row.getIsSelected())
    
      console.log(e)
    }
    </script>
    
    <template>
      <div class=" flex w-full flex-1 gap-1">
        <div class="flex-1">
          <UTable
            ref="table"
            v-model:row-selection="rowSelection"
            :data="data"
            :columns="columns"
            @select="onSelect"
          />
    
          <div class="px-4 py-3.5 border-t border-accented text-sm text-muted">
            {{ table?.tableApi?.getFilteredSelectedRowModel().rows.length || 0 }} of
            {{ table?.tableApi?.getFilteredRowModel().rows.length || 0 }} row(s) selected.
          </div>
        </div>
      </div>
    </template>
    

Expand code

### With column sorting

You can update a column `header` to render a [Button](/components/button)
component inside the `header` to toggle the sorting state using the TanStack
Table [Sorting
APIs](https://tanstack.com/table/latest/docs/api/features/sorting).

#| Date| Status| Email| Amount  
---|---|---|---|---  
#4597| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
#4596| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00  
#4600| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
#4599| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €276.00  
#4598| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €315.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    
    const UBadge = resolveComponent('UBadge')
    const UButton = resolveComponent('UButton')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: ({ column }) => {
          const isSorted = column.getIsSorted()
    
          return h(UButton, {
            color: 'neutral',
            variant: 'ghost',
            label: 'Email',
            icon: isSorted
              ? isSorted === 'asc'
                ? 'i-lucide-arrow-up-narrow-wide'
                : 'i-lucide-arrow-down-wide-narrow'
              : 'i-lucide-arrow-up-down',
            class: '-mx-2.5',
            onClick: () => column.toggleSorting(column.getIsSorted() === 'asc')
          })
        }
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const sorting = ref([
      {
        id: 'email',
        desc: false
      }
    ])
    </script>
    
    <template>
      <UTable v-model:sorting="sorting" :data="data" :columns="columns" class="flex-1" />
    </template>
    

Expand code

You can use the `sorting` prop to control the sorting state of the columns
(can be binded with `v-model`).

You can also create a reusable component to make any column header sortable.

ID| Date| Status| Email| Amount  
---|---|---|---|---  
#4596| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00  
#4597| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
#4598| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €315.00  
#4599| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €276.00  
#4600| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    import type { Column } from '@tanstack/vue-table'
    
    const UBadge = resolveComponent('UBadge')
    const UButton = resolveComponent('UButton')
    const UDropdownMenu = resolveComponent('UDropdownMenu')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: ({ column }) => getHeader(column, 'ID'),
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: ({ column }) => getHeader(column, 'Date'),
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: ({ column }) => getHeader(column, 'Status'),
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: ({ column }) => getHeader(column, 'Email')
      },
      {
        accessorKey: 'amount',
        header: ({ column }) => h('div', { class: 'text-right' }, getHeader(column, 'Amount')),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    function getHeader(column: Column<Payment>, label: string) {
      const isSorted = column.getIsSorted()
    
      return h(
        UDropdownMenu,
        {
          content: {
            align: 'start'
          },
          'aria-label': 'Actions dropdown',
          items: [
            {
              label: 'Asc',
              type: 'checkbox',
              icon: 'i-lucide-arrow-up-narrow-wide',
              checked: isSorted === 'asc',
              onSelect: () => {
                if (isSorted === 'asc') {
                  column.clearSorting()
                } else {
                  column.toggleSorting(false)
                }
              }
            },
            {
              label: 'Desc',
              icon: 'i-lucide-arrow-down-wide-narrow',
              type: 'checkbox',
              checked: isSorted === 'desc',
              onSelect: () => {
                if (isSorted === 'desc') {
                  column.clearSorting()
                } else {
                  column.toggleSorting(true)
                }
              }
            }
          ]
        },
        () =>
          h(UButton, {
            color: 'neutral',
            variant: 'ghost',
            label,
            icon: isSorted
              ? isSorted === 'asc'
                ? 'i-lucide-arrow-up-narrow-wide'
                : 'i-lucide-arrow-down-wide-narrow'
              : 'i-lucide-arrow-up-down',
            class: '-mx-2.5 data-[state=open]:bg-elevated',
            'aria-label': `Sort by ${isSorted === 'asc' ? 'descending' : 'ascending'}`
          })
      )
    }
    
    const sorting = ref([
      {
        id: 'id',
        desc: false
      }
    ])
    </script>
    
    <template>
      <UTable v-model:sorting="sorting" :data="data" :columns="columns" class="flex-1" />
    </template>
    

Expand code

In this example, we use a function to define the column header but you can
also create an actual component.

### With column pinning

You can update a column `header` to render a [Button](/components/button)
component inside the `header` to toggle the pinning state using the TanStack
Table [Pinning APIs](https://tanstack.com/table/latest/docs/api/features/row-
pinning).

A pinned column will become sticky on the left or right side of the table.

ID| Date| Status| Email| Amount  
---|---|---|---|---  
#46000000000000000000000000000000000000000| 2024-03-11T15:30:00| paid| [[email
protected]](/cdn-cgi/l/email-protection)| €594,000.00  
#45990000000000000000000000000000000000000| 2024-03-11T10:10:00| failed|
[[email protected]](/cdn-cgi/l/email-protection)| €276,000.00  
#45980000000000000000000000000000000000000| 2024-03-11T08:50:00| refunded|
[[email protected]](/cdn-cgi/l/email-protection)| €315,000.00  
#45970000000000000000000000000000000000000| 2024-03-10T19:45:00| paid| [[email
protected]](/cdn-cgi/l/email-protection)| €5,290,000.00  
#45960000000000000000000000000000000000000| 2024-03-10T15:55:00| paid| [[email
protected]](/cdn-cgi/l/email-protection)| €639,000.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    import type { Column } from '@tanstack/vue-table'
    
    const UBadge = resolveComponent('UBadge')
    const UButton = resolveComponent('UButton')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '46000000000000000000000000000000000000000',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594000
      },
      {
        id: '45990000000000000000000000000000000000000',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276000
      },
      {
        id: '45980000000000000000000000000000000000000',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315000
      },
      {
        id: '45970000000000000000000000000000000000000',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 5290000
      },
      {
        id: '45960000000000000000000000000000000000000',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639000
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: ({ column }) => getHeader(column, 'ID', 'left'),
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: ({ column }) => getHeader(column, 'Date', 'left')
      },
      {
        accessorKey: 'status',
        header: ({ column }) => getHeader(column, 'Status', 'left'),
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: ({ column }) => getHeader(column, 'Email', 'left')
      },
      {
        accessorKey: 'amount',
        header: ({ column }) => h('div', { class: 'text-right' }, getHeader(column, 'Amount', 'right')),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    function getHeader(column: Column<Payment>, label: string, position: 'left' | 'right') {
      const isPinned = column.getIsPinned()
    
      return h(UButton, {
        color: 'neutral',
        variant: 'ghost',
        label,
        icon: isPinned ? 'i-lucide-pin-off' : 'i-lucide-pin',
        class: '-mx-2.5',
        onClick() {
          column.pin(isPinned === position ? false : position)
        }
      })
    }
    
    const columnPinning = ref({
      left: [],
      right: ['amount']
    })
    </script>
    
    <template>
      <UTable v-model:column-pinning="columnPinning" :data="data" :columns="columns" class="flex-1" />
    </template>
    

Expand code

You can use the `column-pinning` prop to control the pinning state of the
columns (can be binded with `v-model`).

### With column visibility

You can use a [DropdownMenu](/components/dropdown-menu) component to toggle
the visibility of the columns using the TanStack Table [Column Visibility
APIs](https://tanstack.com/table/latest/docs/api/features/column-visibility).

Columns

Date| Status| Email| Amount  
---|---|---|---  
Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)| €594.00  
Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-protection)|
€276.00  
Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-protection)|
€315.00  
Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)| €529.00  
Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)| €639.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import { upperFirst } from 'scule'
    import type { TableColumn } from '@nuxt/ui'
    
    const UBadge = resolveComponent('UBadge')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const table = useTemplateRef('table')
    
    const columnVisibility = ref({
      id: false
    })
    </script>
    
    <template>
      <div class="flex flex-col flex-1 w-full">
        <div class="flex justify-end px-4 py-3.5 border-b  border-accented">
          <UDropdownMenu
            :items="
              table?.tableApi
                ?.getAllColumns()
                .filter((column) => column.getCanHide())
                .map((column) => ({
                  label: upperFirst(column.id),
                  type: 'checkbox' as const,
                  checked: column.getIsVisible(),
                  onUpdateChecked(checked: boolean) {
                    table?.tableApi?.getColumn(column.id)?.toggleVisibility(!!checked)
                  },
                  onSelect(e?: Event) {
                    e?.preventDefault()
                  }
                }))
            "
            :content="{ align: 'end' }"
          >
            <UButton
              label="Columns"
              color="neutral"
              variant="outline"
              trailing-icon="i-lucide-chevron-down"
            />
          </UDropdownMenu>
        </div>
    
        <UTable
          ref="table"
          v-model:column-visibility="columnVisibility"
          :data="data"
          :columns="columns"
        />
      </div>
    </template>
    

Expand code

You can use the `column-visibility` prop to control the visibility state of
the columns (can be binded with `v-model`).

### With column filters

You can use an [Input](/components/input) component to filter per column the
rows using the TanStack Table [Column Filtering
APIs](https://tanstack.com/table/latest/docs/api/features/column-filtering).

#| Date| Status| Email| Amount  
---|---|---|---|---  
#4600| Mar 11, 15:30| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    
    const UBadge = resolveComponent('UBadge')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const table = useTemplateRef('table')
    
    const columnFilters = ref([
      {
        id: 'email',
        value: 'james'
      }
    ])
    </script>
    
    <template>
      <div class="flex flex-col flex-1 w-full">
        <div class="flex px-4 py-3.5 border-b border-accented">
          <UInput
            :model-value="table?.tableApi?.getColumn('email')?.getFilterValue() as string"
            class="max-w-sm"
            placeholder="Filter emails..."
            @update:model-value="table?.tableApi?.getColumn('email')?.setFilterValue($event)"
          />
        </div>
    
        <UTable ref="table" v-model:column-filters="columnFilters" :data="data" :columns="columns" />
      </div>
    </template>
    

Expand code

You can use the `column-filters` prop to control the filters state of the
columns (can be binded with `v-model`).

### With global filter

You can use an [Input](/components/input) component to filter the rows using
the TanStack Table [Global Filtering
APIs](https://tanstack.com/table/latest/docs/api/features/global-filtering).

#| Date| Status| Email| Amount  
---|---|---|---|---  
#4599| Mar 11, 10:10| failed| [[email protected]](/cdn-cgi/l/email-
protection)| €276.00  
#4598| Mar 11, 08:50| refunded| [[email protected]](/cdn-cgi/l/email-
protection)| €315.00  
#4597| Mar 10, 19:45| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
#4596| Mar 10, 15:55| paid| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00  
      
    
    <script setup lang="ts">
    import { h, resolveComponent } from 'vue'
    import type { TableColumn } from '@nuxt/ui'
    
    const UBadge = resolveComponent('UBadge')
    
    type Payment = {
      id: string
      date: string
      status: 'paid' | 'failed' | 'refunded'
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        status: 'failed',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        status: 'refunded',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        status: 'paid',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
          const color = {
            paid: 'success' as const,
            failed: 'error' as const,
            refunded: 'neutral' as const
          }[row.getValue('status') as string]
    
          return h(UBadge, { class: 'capitalize', variant: 'subtle', color }, () =>
            row.getValue('status')
          )
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
    
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
    
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const globalFilter = ref('45')
    </script>
    
    <template>
      <div class="flex flex-col flex-1 w-full">
        <div class="flex px-4 py-3.5 border-b border-accented">
          <UInput v-model="globalFilter" class="max-w-sm" placeholder="Filter..." />
        </div>
    
        <UTable ref="table" v-model:global-filter="globalFilter" :data="data" :columns="columns" />
      </div>
    </template>
    

Expand code

You can use the `global-filter` prop to control the global filter state (can
be binded with `v-model`).

### With pagination

You can use a [Pagination](/components/pagination) component to control the
pagination state using the [Pagination
APIs](https://tanstack.com/table/latest/docs/api/features/pagination).

There are different pagination approaches as explained in [Pagination
Guide](https://tanstack.com/table/latest/docs/guide/pagination#pagination-
guide). In this example, we use client-side pagination so we need to manually
pass `getPaginationRowModel()` function.

#| Date| Email| Amount  
---|---|---|---  
#4600| Mar 11, 15:30| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
#4599| Mar 11, 10:10| [[email protected]](/cdn-cgi/l/email-protection)|
€276.00  
#4598| Mar 11, 08:50| [[email protected]](/cdn-cgi/l/email-protection)|
€315.00  
#4597| Mar 10, 19:45| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
#4596| Mar 10, 15:55| [[email protected]](/cdn-cgi/l/email-protection)|
€639.00  
      
    
    <script setup lang="ts">
    import { getPaginationRowModel } from '@tanstack/vue-table'
    import type { TableColumn } from '@nuxt/ui'
    
    const table = useTemplateRef('table')
    
    type Payment = {
      id: string
      date: string
      email: string
      amount: number
    }
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      },
      {
        id: '4596',
        date: '2024-03-10T15:55:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 639
      },
      {
        id: '4595',
        date: '2024-03-10T13:20:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 428
      },
      {
        id: '4594',
        date: '2024-03-10T11:05:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 673
      },
      {
        id: '4593',
        date: '2024-03-09T22:15:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 382
      },
      {
        id: '4592',
        date: '2024-03-09T20:30:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 547
      },
      {
        id: '4591',
        date: '2024-03-09T18:45:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 291
      },
      {
        id: '4590',
        date: '2024-03-09T16:20:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 624
      },
      {
        id: '4589',
        date: '2024-03-09T14:10:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 438
      },
      {
        id: '4588',
        date: '2024-03-09T12:05:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 583
      },
      {
        id: '4587',
        date: '2024-03-09T10:30:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 347
      },
      {
        id: '4586',
        date: '2024-03-09T08:15:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 692
      },
      {
        id: '4585',
        date: '2024-03-08T23:40:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 419
      },
      {
        id: '4584',
        date: '2024-03-08T21:25:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 563
      },
      {
        id: '4583',
        date: '2024-03-08T19:50:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 328
      },
      {
        id: '4582',
        date: '2024-03-08T17:35:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 647
      },
      {
        id: '4581',
        date: '2024-03-08T15:20:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 482
      }
    ])
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    const pagination = ref({
      pageIndex: 0,
      pageSize: 5
    })
    </script>
    
    <template>
      <div class="w-full space-y-4 pb-4">
        <UTable
          ref="table"
          v-model:pagination="pagination"
          :data="data"
          :columns="columns"
          :pagination-options="{
            getPaginationRowModel: getPaginationRowModel()
          }"
          class="flex-1"
        />
    
        <div class="flex justify-center border-t border-default pt-4">
          <UPagination
            :default-page="(table?.tableApi?.getState().pagination.pageIndex || 0) + 1"
            :items-per-page="table?.tableApi?.getState().pagination.pageSize"
            :total="table?.tableApi?.getFilteredRowModel().rows.length"
            @update:page="(p) => table?.tableApi?.setPageIndex(p - 1)"
          />
        </div>
      </div>
    </template>
    

Expand code

You can use the `pagination` prop to control the pagination state (can be
binded with `v-model`).

### With fetched data

You can fetch data from an API and use them in the Table.

ID| Name| Email| Company  
---|---|---|---  
1| ![Leanne Graham avatar](https://i.pravatar.cc/120?img=1)Leanne Graham@Bret|
[[email protected]](/cdn-cgi/l/email-protection)| Romaguera-Crona  
2| ![Ervin Howell avatar](https://i.pravatar.cc/120?img=2)Ervin
Howell@Antonette| [[email protected]](/cdn-cgi/l/email-protection)| Deckow-
Crist  
3| ![Clementine Bauch avatar](https://i.pravatar.cc/120?img=3)Clementine
Bauch@Samantha| [[email protected]](/cdn-cgi/l/email-protection)| Romaguera-
Jacobson  
4| ![Patricia Lebsack avatar](https://i.pravatar.cc/120?img=4)Patricia
Lebsack@Karianne| [[email protected]](/cdn-cgi/l/email-protection)| Robel-
Corkery  
5| ![Chelsey Dietrich avatar](https://i.pravatar.cc/120?img=5)Chelsey
Dietrich@Kamren| [[email protected]](/cdn-cgi/l/email-protection)| Keebler LLC  
6| ![Mrs. Dennis Schulist avatar](https://i.pravatar.cc/120?img=6)Mrs. Dennis
Schulist@Leopoldo_Corkery| [[email protected]](/cdn-cgi/l/email-protection)|
Considine-Lockman  
7| ![Kurtis Weissnat avatar](https://i.pravatar.cc/120?img=7)Kurtis
Weissnat@Elwyn.Skiles| [[email protected]](/cdn-cgi/l/email-protection)| Johns
Group  
8| ![Nicholas Runolfsdottir V avatar](https://i.pravatar.cc/120?img=8)Nicholas
Runolfsdottir V@Maxime_Nienow| [[email protected]](/cdn-cgi/l/email-
protection)| Abernathy Group  
9| ![Glenna Reichert avatar](https://i.pravatar.cc/120?img=9)Glenna
Reichert@Delphine| [[email protected]](/cdn-cgi/l/email-protection)| Yost and
Sons  
10| ![Clementina DuBuque avatar](https://i.pravatar.cc/120?img=10)Clementina
DuBuque@Moriah.Stanton| [[email protected]](/cdn-cgi/l/email-protection)|
Hoeger LLC  
      
    
    <script setup lang="ts">
    import type { TableColumn } from '@nuxt/ui'
    
    const UAvatar = resolveComponent('UAvatar')
    
    type User = {
      id: number
      name: string
      username: string
      email: string
      avatar: { src: string }
      company: { name: string }
    }
    
    const { data, status } = await useFetch<User[]>('https://jsonplaceholder.typicode.com/users', {
      key: 'table-users',
      transform: (data) => {
        return (
          data?.map((user) => ({
            ...user,
            avatar: { src: `https://i.pravatar.cc/120?img=${user.id}`, alt: `${user.name} avatar` }
          })) || []
        )
      },
      lazy: true
    })
    
    const columns: TableColumn<User>[] = [
      {
        accessorKey: 'id',
        header: 'ID'
      },
      {
        accessorKey: 'name',
        header: 'Name',
        cell: ({ row }) => {
          return h('div', { class: 'flex items-center gap-3' }, [
            h(UAvatar, {
              ...row.original.avatar,
              size: 'lg'
            }),
            h('div', undefined, [
              h('p', { class: 'font-medium text-highlighted' }, row.original.name),
              h('p', { class: '' }, `@${row.original.username}`)
            ])
          ])
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'company',
        header: 'Company',
        cell: ({ row }) => row.original.company.name
      }
    ]
    </script>
    
    <template>
      <UTable :data="data" :columns="columns" :loading="status === 'pending'" class="flex-1" />
    </template>
    

Expand code

### With infinite scroll

If you use server-side pagination, you can use the
[`useInfiniteScroll`](https://vueuse.org/core/useInfiniteScroll/#useinfinitescroll)
composable to load more data when scrolling.

ID| Avatar| First name| Email| Username  
---|---|---|---|---  
No data  
      
    
    <script setup lang="ts">
    import type { TableColumn } from '@nuxt/ui'
    import { useInfiniteScroll } from '@vueuse/core'
    
    const UAvatar = resolveComponent('UAvatar')
    
    type User = {
      id: number
      firstName: string
      username: string
      email: string
      image: string
    }
    
    type UserResponse = {
      users: User[]
      total: number
      skip: number
      limit: number
    }
    
    const skip = ref(0)
    
    const { data, status, execute } = await useFetch(
      'https://dummyjson.com/users?limit=10&select=firstName,username,email,image',
      {
        key: 'table-users-infinite-scroll',
        params: { skip },
        transform: (data?: UserResponse) => {
          return data?.users
        },
        lazy: true,
        immediate: false
      }
    )
    
    const columns: TableColumn<User>[] = [
      {
        accessorKey: 'id',
        header: 'ID'
      },
      {
        accessorKey: 'image',
        header: 'Avatar',
        cell: ({ row }) => h(UAvatar, { src: row.original.image })
      },
      {
        accessorKey: 'firstName',
        header: 'First name'
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'username',
        header: 'Username'
      }
    ]
    
    const users = ref<User[]>([])
    
    watch(data, () => {
      users.value = [...users.value, ...(data.value || [])]
    })
    
    execute()
    
    const table = useTemplateRef<ComponentPublicInstance>('table')
    
    onMounted(() => {
      useInfiniteScroll(
        table.value?.$el,
        () => {
          skip.value += 10
        },
        {
          distance: 200,
          canLoadMore: () => {
            return status.value !== 'pending'
          }
        }
      )
    })
    </script>
    
    <template>
      <div class="w-full">
        <UTable
          ref="table"
          :data="users"
          :columns="columns"
          :loading="status === 'pending'"
          sticky
          class="flex-1 h-80"
        />
      </div>
    </template>
    

Expand code

### With drag and drop

Use the [`useSortable`](https://vueuse.org/integrations/useSortable/)
composable from
[`@vueuse/integrations`](https://vueuse.org/integrations/README.html) to
enable drag and drop functionality on the Table. This integration wraps
[Sortable.js](https://sortablejs.github.io/Sortable/) to provide a seamless
drag and drop experience.

Since the table ref doesn't expose the tbody element, add a unique class to it
via the `:ui` prop to target it with `useSortable` (e.g. `:ui="{ tbody: 'my-
table-tbody' }"`).

#| Date| Email| Amount  
---|---|---|---  
#4600| Mar 11, 15:30| [[email protected]](/cdn-cgi/l/email-protection)|
€594.00  
#4599| Mar 11, 10:10| [[email protected]](/cdn-cgi/l/email-protection)|
€276.00  
#4598| Mar 11, 08:50| [[email protected]](/cdn-cgi/l/email-protection)|
€315.00  
#4597| Mar 10, 19:45| [[email protected]](/cdn-cgi/l/email-protection)|
€529.00  
      
    
    <script setup lang="ts">
    import type { TableColumn } from '@nuxt/ui'
    import { useSortable } from '@vueuse/integrations/useSortable.mjs'
    
    type Payment = {
      id: string
      date: string
      email: string
      amount: number
    }
    
    const data = ref<Payment[]>([
      {
        id: '4600',
        date: '2024-03-11T15:30:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 594
      },
      {
        id: '4599',
        date: '2024-03-11T10:10:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 276
      },
      {
        id: '4598',
        date: '2024-03-11T08:50:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 315
      },
      {
        id: '4597',
        date: '2024-03-10T19:45:00',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        amount: 529
      }
    ])
    
    const columns: TableColumn<Payment>[] = [
      {
        accessorKey: 'id',
        header: '#',
        cell: ({ row }) => `#${row.getValue('id')}`
      },
      {
        accessorKey: 'date',
        header: 'Date',
        cell: ({ row }) => {
          return new Date(row.getValue('date')).toLocaleString('en-US', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          })
        }
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'amount',
        header: () => h('div', { class: 'text-right' }, 'Amount'),
        cell: ({ row }) => {
          const amount = Number.parseFloat(row.getValue('amount'))
          const formatted = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR'
          }).format(amount)
          return h('div', { class: 'text-right font-medium' }, formatted)
        }
      }
    ]
    
    useSortable('.my-table-tbody', data, {
      animation: 150
    })
    </script>
    
    <template>
      <div class="w-full">
        <UTable
          ref="table"
          :data="data"
          :columns="columns"
          :ui="{
            tbody: 'my-table-tbody'
          }"
        />
      </div>
    </template>
    

Expand code

### With slots

You can use slots to customize the header and data cells of the table.

Use the `#<column>-header` slot to customize the header of a column. You will
have access to the `column`, `header` and `table` properties in the slot
scope.

Use the `#<column>-cell` slot to customize the cell of a column. You will have
access to the `cell`, `column`, `getValue`, `renderValue`, `row`, and `table`
properties in the slot scope.

ID| Name| Email| Role|  
---|---|---|---|---  
1| ![Lindsay Walton avatar](https://i.pravatar.cc/120?img=1)Lindsay
WaltonFront-end Developer| [[email protected]](/cdn-cgi/l/email-protection)|
Member|  
2| ![Courtney Henry avatar](https://i.pravatar.cc/120?img=2)Courtney
HenryDesigner| [[email protected]](/cdn-cgi/l/email-protection)| Admin|  
3| ![Tom Cook avatar](https://i.pravatar.cc/120?img=3)Tom CookDirector of
Product| [[email protected]](/cdn-cgi/l/email-protection)| Member|  
4| ![Whitney Francis avatar](https://i.pravatar.cc/120?img=4)Whitney
FrancisCopywriter| [[email protected]](/cdn-cgi/l/email-protection)| Admin|  
5| ![Leonard Krasner avatar](https://i.pravatar.cc/120?img=5)Leonard
KrasnerSenior Designer| [[email protected]](/cdn-cgi/l/email-protection)|
Owner|  
6| ![Floyd Miles avatar](https://i.pravatar.cc/120?img=6)Floyd MilesPrincipal
Designer| [[email protected]](/cdn-cgi/l/email-protection)| Member|  
      
    
    <script setup lang="ts">
    import type { TableColumn, DropdownMenuItem } from '@nuxt/ui'
    
    interface User {
      id: number
      name: string
      position: string
      email: string
      role: string
    }
    
    const toast = useToast()
    
    const data = ref<User[]>([
      {
        id: 1,
        name: 'Lindsay Walton',
        position: 'Front-end Developer',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        role: 'Member'
      },
      {
        id: 2,
        name: 'Courtney Henry',
        position: 'Designer',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        role: 'Admin'
      },
      {
        id: 3,
        name: 'Tom Cook',
        position: 'Director of Product',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        role: 'Member'
      },
      {
        id: 4,
        name: 'Whitney Francis',
        position: 'Copywriter',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        role: 'Admin'
      },
      {
        id: 5,
        name: 'Leonard Krasner',
        position: 'Senior Designer',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        role: 'Owner'
      },
      {
        id: 6,
        name: 'Floyd Miles',
        position: 'Principal Designer',
        email: '[[email protected]](/cdn-cgi/l/email-protection)',
        role: 'Member'
      }
    ])
    
    const columns: TableColumn<User>[] = [
      {
        accessorKey: 'id',
        header: 'ID'
      },
      {
        accessorKey: 'name',
        header: 'Name'
      },
      {
        accessorKey: 'email',
        header: 'Email'
      },
      {
        accessorKey: 'role',
        header: 'Role'
      },
      {
        id: 'action'
      }
    ]
    
    function getDropdownActions(user: User): DropdownMenuItem[][] {
      return [
        [
          {
            label: 'Copy user Id',
            icon: 'i-lucide-copy',
            onSelect: () => {
              navigator.clipboard.writeText(user.id.toString())
              toast.add({
                title: 'User ID copied to clipboard!',
                color: 'success',
                icon: 'i-lucide-circle-check'
              })
            }
          }
        ],
        [
          {
            label: 'Edit',
            icon: 'i-lucide-edit'
          },
          {
            label: 'Delete',
            icon: 'i-lucide-trash',
            color: 'error'
          }
        ]
      ]
    }
    </script>
    
    <template>
      <UTable :data="data" :columns="columns" class="flex-1">
        <template #name-cell="{ row }">
          <div class="flex items-center gap-3">
            <UAvatar
              :src="`https://i.pravatar.cc/120?img=${row.original.id}`"
              size="lg"
              :alt="`${row.original.name} avatar`"
            />
            <div>
              <p class="font-medium text-highlighted">
                {{ row.original.name }}
              </p>
              <p>
                {{ row.original.position }}
              </p>
            </div>
          </div>
        </template>
        <template #action-cell="{ row }">
          <UDropdownMenu :items="getDropdownActions(row.original)">
            <UButton
              icon="i-lucide-ellipsis-vertical"
              color="neutral"
              variant="ghost"
              aria-label="Actions"
            />
          </UDropdownMenu>
        </template>
      </UTable>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`data`| | ` unknown[]`  
`columns`| | ` TableColumn<unknown, unknown>[]`Show properties

  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `header: string`
  * `id?: string`
  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `id: string`
  * `header?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `columns?: ColumnDef<unknown, any>[]`
  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `header: string`
  * `id?: string`
  * `columns?: ColumnDef<unknown, any>[]`
  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `id: string`
  * `header?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `id?: string`
  * `accessorKey: string & {}`
  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `header?: string`
  * `id?: string`
  * `accessorKey: string & {}`
  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `header?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `accessorFn: AccessorFn<unknown, unknown>`
  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `header: string`
  * `id?: string`
  * `accessorFn: AccessorFn<unknown, unknown>`
  * `getUniqueValues?: AccessorFn<unknown, unknown[]>`
  * `footer?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`
  * `cell?: ColumnDefTemplate<CellContext<unknown, unknown>>`
  * `meta?: ColumnMeta<unknown, unknown>`
  * `enableHiding?: boolean`
  * `enablePinning?: boolean`Enables/disables column pinning for this column. Defaults to `true`.
  * `enableColumnFilter?: boolean`Enables/disables the **column** filter for this column.
  * `filterFn?: FilterFnOption<unknown>`The filter function to use with this column. Can be the name of a built-in filter function or a custom filter function.
  * `enableGlobalFilter?: boolean`Enables/disables the **global** filter for this column.
  * `enableMultiSort?: boolean`Enables/Disables multi-sorting for this column.
  * `enableSorting?: boolean`Enables/Disables sorting for this column.
  * `invertSorting?: boolean`Inverts the order of the sorting for this column. This is useful for values that have an inverted best/worst scale where lower numbers are better, eg. a ranking (1st, 2nd, 3rd) or golf-like scoring
  * `sortDescFirst?: boolean`Set to `true` for sorting toggles on this column to start in the descending direction.
  * `sortingFn?: SortingFnOption<unknown>`The sorting function to use with this column.
    * A `string` referencing a built-in sorting function
    * A custom sorting function
  * `sortUndefined?: false | 1 | -1 | "first" | "last"`The priority of undefined values when sorting this column.
    * `false`
      * Undefined values will be considered tied and need to be sorted by the next column filter or original index (whichever applies)
    * `-1`
      * Undefined values will be sorted with higher priority (ascending) (if ascending, undefined will appear on the beginning of the list)
    * `1`
      * Undefined values will be sorted with lower priority (descending) (if ascending, undefined will appear on the end of the list)
  * `aggregatedCell?: ColumnDefTemplate<CellContext<unknown, unknown>>`The cell to display each row for the column if the cell is an aggregate. If a function is passed, it will be passed a props object with the context of the cell and should return the property type for your adapter (the exact type depends on the adapter being used).
  * `aggregationFn?: AggregationFnOption<unknown>`The resolved aggregation function for the column.
  * `enableGrouping?: boolean`Enables/disables grouping for this column.
  * `getGroupingValue?: ((row: unknown) => any)`Specify a value to be used for grouping rows on this column. If this option is not specified, the value derived from `accessorKey` / `accessorFn` will be used instead.
  * `enableResizing?: boolean`Enables or disables column resizing for the column.
  * `maxSize?: number`The maximum allowed size for the column
  * `minSize?: number`The minimum allowed size for the column
  * `size?: number`The desired size for the column
  * `id: string`
  * `header?: ColumnDefTemplate<HeaderContext<unknown, unknown>>`

  
`caption`| | ` string`  
`meta`| | ` TableMeta<unknown>`You can pass any object to `options.meta` and access it anywhere the `table` is available via `table.options.meta`.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#meta)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`empty`| `t('table.noData')`| ` string`The text to display when the table is
empty.  
`sticky`| `false`| `boolean`Whether the table should have a sticky header.  
`loading`| | `boolean`Whether the table should be in loading state.  
`loadingColor`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`loadingAnimation`| `'carousel'`| ` "carousel" | "carousel-inverse" | "swing" | "elastic"`  
`watchOptions`| `{ deep: true }`| ` WatchOptions<boolean>`Use the
`watchOptions` prop to customize reactivity (for ex: disable deep watching for
changes in your data or limiting the max traversal depth). This can improve
performance by reducing unnecessary re-renders, but it should be used with
caution as it may lead to unexpected behavior if not managed properly.

  * [API Docs](https://vuejs.org/api/options-state.html#watch)
  * [Guide](https://vuejs.org/guide/essentials/watchers.html)

  
`globalFilterOptions`| | ` Omit<GlobalFilterOptions<unknown>, "onGlobalFilterChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/global-filtering#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/global-filtering)

  
`columnFiltersOptions`| | ` Omit<ColumnFiltersOptions<unknown>, "getFilteredRowModel" | "onColumnFiltersChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/column-filtering#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/column-filtering)

  
`columnPinningOptions`| | ` Omit<ColumnPinningOptions, "onColumnPinningChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/column-pinning#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/column-pinning)

  
`columnSizingOptions`| | ` Omit<ColumnSizingOptions, "onColumnSizingChange" | "onColumnSizingInfoChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/column-sizing#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/column-sizing)

  
`visibilityOptions`| | ` Omit<VisibilityOptions, "onColumnVisibilityChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/column-visibility#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/column-visibility)

  
`sortingOptions`| | ` Omit<SortingOptions<unknown>, "getSortedRowModel" | "onSortingChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/sorting#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/sorting)

  
`groupingOptions`| | ` Omit<GroupingOptions, "onGroupingChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/grouping#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/grouping)

  
`expandedOptions`| | ` Omit<ExpandedOptions<unknown>, "getExpandedRowModel" | "onExpandedChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/expanding#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/expanding)

  
`rowSelectionOptions`| | ` Omit<RowSelectionOptions<unknown>, "onRowSelectionChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/row-selection#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/row-selection)

  
`rowPinningOptions`| | ` Omit<RowPinningOptions<unknown>, "onRowPinningChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/row-pinning#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/row-pinning)

  
`paginationOptions`| | ` Omit<PaginationOptions, "onPaginationChange">`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/pagination#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/pagination)

  
`facetedOptions`| | ` FacetedOptions<unknown>`

  * [API Docs](https://tanstack.com/table/v8/docs/api/features/column-faceting#table-options)
  * [Guide](https://tanstack.com/table/v8/docs/guide/column-faceting)

  
`state`| | ` Partial<TableState>`  
`renderFallbackValue`| | `any`  
`_features`| | ` TableFeature<any>[]`An array of extra features that you can add to the table instance.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#_features)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`autoResetAll`| | `boolean`Set this option to override any of the `autoReset...` feature options.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#autoresetall)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`debugAll`| | `boolean`Set this option to `true` to output all debugging information to the console.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#debugall)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`debugCells`| | `boolean`Set this option to `true` to output cell debugging information to the console.

  * [API Docs](<https://tanstack.com/table/v8/docs/api/core/table#debugcells>]
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`debugColumns`| | `boolean`Set this option to `true` to output column debugging information to the console.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#debugcolumns)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`debugHeaders`| | `boolean`Set this option to `true` to output header debugging information to the console.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#debugheaders)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`debugRows`| | `boolean`Set this option to `true` to output row debugging information to the console.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#debugrows)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`debugTable`| | `boolean`Set this option to `true` to output table debugging information to the console.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#debugtable)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`defaultColumn`| | ` Partial<ColumnDefBase<unknown, unknown> & StringHeaderIdentifier> | Partial<ColumnDefBase<unknown, unknown> & IdIdentifier<unknown, unknown>> | Partial<GroupColumnDefBase<unknown, unknown> & StringHeaderIdentifier> | Partial<GroupColumnDefBase<unknown, unknown> & IdIdentifier<unknown, unknown>> | Partial<AccessorKeyColumnDefBase<unknown, unknown> & Partial<StringHeaderIdentifier>> | Partial<AccessorKeyColumnDefBase<unknown, unknown> & Partial<IdIdentifier<unknown, unknown>>> | Partial<AccessorFnColumnDefBase<unknown, unknown> & StringHeaderIdentifier> | Partial<AccessorFnColumnDefBase<unknown, unknown> & IdIdentifier<unknown, unknown>>`Default column options to use for all column defs supplied to the table.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#defaultcolumn)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`getRowId`| | ` (originalRow: unknown, index: number, parent?: Row<unknown> | undefined): string`This optional function is used to derive a unique ID for any given row. If not provided the rows index is used (nested rows join together with `.` using their grandparents' index eg. `index.index.index`). If you need to identify individual rows that are originating from any server-side operations, it's suggested you use this function to return an ID that makes sense regardless of network IO/ambiguity eg. a userId, taskId, database ID field, etc.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#getrowid)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`getSubRows`| | `(originalRow: unknown, index: number): unknown[]`This optional function is used to access the sub rows for any given row. If you are using nested rows, you will need to use this function to return the sub rows object (or undefined) from the row.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#getsubrows)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`initialState`| | ` InitialTableState`Use this option to optionally pass initial state to the table. This state will be used when resetting various table states either automatically by the table (eg. `options.autoResetPageIndex`) or via functions like `table.resetRowSelection()`. Most reset function allow you optionally pass a flag to reset to a blank/default state instead of the initial state.Table state will not be reset when this object changes, which also means that the initial state object does not need to be stable.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#initialstate)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

Show properties

  * `columnVisibility?: VisibilityState`
  * `columnOrder?: ColumnOrderState`
  * `columnPinning?: ColumnPinningState`
  * `rowPinning?: RowPinningState`
  * `columnFilters?: ColumnFiltersState`
  * `globalFilter?: any`
  * `sorting?: SortingState`
  * `expanded?: ExpandedState`
  * `grouping?: GroupingState`
  * `columnSizing?: ColumnSizingState`
  * `columnSizingInfo?: ColumnSizingInfoState`
  * `pagination?: Partial<PaginationState>`
  * `rowSelection?: RowSelectionState`

  
`mergeOptions`| | ` (defaultOptions: TableOptions<unknown>, options: Partial<TableOptions<unknown>>): TableOptions<unknown>`This option is used to optionally implement the merging of table options.

  * [API Docs](https://tanstack.com/table/v8/docs/api/core/table#mergeoptions)
  * [Guide](https://tanstack.com/table/v8/docs/guide/tables)

  
`globalFilter`| `undefined`| ` string`  
`columnFilters`| `[]`| ` ColumnFiltersState`Show properties

  * `id: string`
  * `value: unknown`

  
`columnOrder`| `[]`| ` ColumnOrderState`  
`columnVisibility`| `{}`| ` VisibilityState`  
`columnPinning`| `{}`| ` ColumnPinningState`Show properties

  * `left?: string[]`
  * `right?: string[]`

  
`columnSizing`| `{}`| ` ColumnSizingState`  
`columnSizingInfo`| `{}`| ` ColumnSizingInfoState`Show properties

  * `columnSizingStart: [string, number][]`
  * `deltaOffset: number | null`
  * `deltaPercentage: number | null`
  * `isResizingColumn: string | false`
  * `startOffset: number | null`
  * `startSize: number | null`

  
`rowSelection`| `{}`| ` RowSelectionState`  
`rowPinning`| `{}`| ` RowPinningState`Show properties

  * `bottom?: string[]`
  * `top?: string[]`

  
`sorting`| `[]`| ` SortingState`Show properties

  * `desc: boolean`
  * `id: string`

  
`grouping`| `[]`| ` GroupingState`  
`expanded`| `{}`| ` true | Record<string, boolean>`  
`pagination`| `{}`| ` PaginationState`Show properties

  * `pageIndex: number`
  * `pageSize: number`

  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; caption?: ClassNameValue; thead?: ClassNameValue; tbody?: ClassNameValue; ... 4 more ...; loading?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`expanded`| `{ row: Row<unknown>; }`  
`empty`| `{}`  
`loading`| `{}`  
`caption`| `{}`  
  
### Expose

You can access the typed component instance using
[`useTemplateRef`](https://vuejs.org/api/composition-api-
helpers.html#usetemplateref).

    
    
    <script setup lang="ts">
    const table = useTemplateRef('table')
    </script>
    
    <template>
      <UTable ref="table" />
    </template>
    

This will give you access to the following:

Name| Type  
---|---  
`tableRef`| `Ref<HTMLTableElement | null>`  
`tableApi`| [`Ref<Table | null>`](https://tanstack.com/table/latest/docs/api/core/table#table-api)  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        table: {
          slots: {
            root: 'relative overflow-auto',
            base: 'min-w-full overflow-clip',
            caption: 'sr-only',
            thead: 'relative [&>tr]:after:absolute [&>tr]:after:inset-x-0 [&>tr]:after:bottom-0 [&>tr]:after:h-px [&>tr]:after:bg-(--ui-border-accented)',
            tbody: 'divide-y divide-default [&>tr]:data-[selectable=true]:hover:bg-elevated/50 [&>tr]:data-[selectable=true]:focus-visible:outline-primary',
            tr: 'data-[selected=true]:bg-elevated/50',
            th: 'px-4 py-3.5 text-sm text-highlighted text-left rtl:text-right font-semibold [&:has([role=checkbox])]:pe-0',
            td: 'p-4 text-sm text-muted whitespace-nowrap [&:has([role=checkbox])]:pe-0',
            empty: 'py-6 text-center text-sm text-muted',
            loading: 'py-6 text-center'
          },
          variants: {
            pinned: {
              true: {
                th: 'sticky bg-default/75 data-[pinned=left]:left-0 data-[pinned=right]:right-0',
                td: 'sticky bg-default/75 data-[pinned=left]:left-0 data-[pinned=right]:right-0'
              }
            },
            sticky: {
              true: {
                thead: 'sticky top-0 inset-x-0 bg-default/75 z-[1] backdrop-blur'
              }
            },
            loading: {
              true: {
                thead: 'after:absolute after:bottom-0 after:inset-x-0 after:h-px'
              }
            },
            loadingAnimation: {
              carousel: '',
              'carousel-inverse': '',
              swing: '',
              elastic: ''
            },
            loadingColor: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            }
          },
          compoundVariants: [
            {
              loading: true,
              loadingColor: 'primary',
              class: {
                thead: 'after:bg-primary'
              }
            },
            {
              loading: true,
              loadingColor: 'neutral',
              class: {
                thead: 'after:bg-inverted'
              }
            },
            {
              loading: true,
              loadingAnimation: 'carousel',
              class: {
                thead: 'after:animate-[carousel_2s_ease-in-out_infinite] rtl:after:animate-[carousel-rtl_2s_ease-in-out_infinite]'
              }
            },
            {
              loading: true,
              loadingAnimation: 'carousel-inverse',
              class: {
                thead: 'after:animate-[carousel-inverse_2s_ease-in-out_infinite] rtl:after:animate-[carousel-inverse-rtl_2s_ease-in-out_infinite]'
              }
            },
            {
              loading: true,
              loadingAnimation: 'swing',
              class: {
                thead: 'after:animate-[swing_2s_ease-in-out_infinite]'
              }
            },
            {
              loading: true,
              loadingAnimation: 'elastic',
              class: {
                thead: 'after:animate-[elastic_2s_ease-in-out_infinite]'
              }
            }
          ],
          defaultVariants: {
            loadingColor: 'primary',
            loadingAnimation: 'carousel'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            table: {
              slots: {
                root: 'relative overflow-auto',
                base: 'min-w-full overflow-clip',
                caption: 'sr-only',
                thead: 'relative [&>tr]:after:absolute [&>tr]:after:inset-x-0 [&>tr]:after:bottom-0 [&>tr]:after:h-px [&>tr]:after:bg-(--ui-border-accented)',
                tbody: 'divide-y divide-default [&>tr]:data-[selectable=true]:hover:bg-elevated/50 [&>tr]:data-[selectable=true]:focus-visible:outline-primary',
                tr: 'data-[selected=true]:bg-elevated/50',
                th: 'px-4 py-3.5 text-sm text-highlighted text-left rtl:text-right font-semibold [&:has([role=checkbox])]:pe-0',
                td: 'p-4 text-sm text-muted whitespace-nowrap [&:has([role=checkbox])]:pe-0',
                empty: 'py-6 text-center text-sm text-muted',
                loading: 'py-6 text-center'
              },
              variants: {
                pinned: {
                  true: {
                    th: 'sticky bg-default/75 data-[pinned=left]:left-0 data-[pinned=right]:right-0',
                    td: 'sticky bg-default/75 data-[pinned=left]:left-0 data-[pinned=right]:right-0'
                  }
                },
                sticky: {
                  true: {
                    thead: 'sticky top-0 inset-x-0 bg-default/75 z-[1] backdrop-blur'
                  }
                },
                loading: {
                  true: {
                    thead: 'after:absolute after:bottom-0 after:inset-x-0 after:h-px'
                  }
                },
                loadingAnimation: {
                  carousel: '',
                  'carousel-inverse': '',
                  swing: '',
                  elastic: ''
                },
                loadingColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                }
              },
              compoundVariants: [
                {
                  loading: true,
                  loadingColor: 'primary',
                  class: {
                    thead: 'after:bg-primary'
                  }
                },
                {
                  loading: true,
                  loadingColor: 'neutral',
                  class: {
                    thead: 'after:bg-inverted'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'carousel',
                  class: {
                    thead: 'after:animate-[carousel_2s_ease-in-out_infinite] rtl:after:animate-[carousel-rtl_2s_ease-in-out_infinite]'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'carousel-inverse',
                  class: {
                    thead: 'after:animate-[carousel-inverse_2s_ease-in-out_infinite] rtl:after:animate-[carousel-inverse-rtl_2s_ease-in-out_infinite]'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'swing',
                  class: {
                    thead: 'after:animate-[swing_2s_ease-in-out_infinite]'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'elastic',
                  class: {
                    thead: 'after:animate-[elastic_2s_ease-in-out_infinite]'
                  }
                }
              ],
              defaultVariants: {
                loadingColor: 'primary',
                loadingAnimation: 'carousel'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            table: {
              slots: {
                root: 'relative overflow-auto',
                base: 'min-w-full overflow-clip',
                caption: 'sr-only',
                thead: 'relative [&>tr]:after:absolute [&>tr]:after:inset-x-0 [&>tr]:after:bottom-0 [&>tr]:after:h-px [&>tr]:after:bg-(--ui-border-accented)',
                tbody: 'divide-y divide-default [&>tr]:data-[selectable=true]:hover:bg-elevated/50 [&>tr]:data-[selectable=true]:focus-visible:outline-primary',
                tr: 'data-[selected=true]:bg-elevated/50',
                th: 'px-4 py-3.5 text-sm text-highlighted text-left rtl:text-right font-semibold [&:has([role=checkbox])]:pe-0',
                td: 'p-4 text-sm text-muted whitespace-nowrap [&:has([role=checkbox])]:pe-0',
                empty: 'py-6 text-center text-sm text-muted',
                loading: 'py-6 text-center'
              },
              variants: {
                pinned: {
                  true: {
                    th: 'sticky bg-default/75 data-[pinned=left]:left-0 data-[pinned=right]:right-0',
                    td: 'sticky bg-default/75 data-[pinned=left]:left-0 data-[pinned=right]:right-0'
                  }
                },
                sticky: {
                  true: {
                    thead: 'sticky top-0 inset-x-0 bg-default/75 z-[1] backdrop-blur'
                  }
                },
                loading: {
                  true: {
                    thead: 'after:absolute after:bottom-0 after:inset-x-0 after:h-px'
                  }
                },
                loadingAnimation: {
                  carousel: '',
                  'carousel-inverse': '',
                  swing: '',
                  elastic: ''
                },
                loadingColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                }
              },
              compoundVariants: [
                {
                  loading: true,
                  loadingColor: 'primary',
                  class: {
                    thead: 'after:bg-primary'
                  }
                },
                {
                  loading: true,
                  loadingColor: 'neutral',
                  class: {
                    thead: 'after:bg-inverted'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'carousel',
                  class: {
                    thead: 'after:animate-[carousel_2s_ease-in-out_infinite] rtl:after:animate-[carousel-rtl_2s_ease-in-out_infinite]'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'carousel-inverse',
                  class: {
                    thead: 'after:animate-[carousel-inverse_2s_ease-in-out_infinite] rtl:after:animate-[carousel-inverse-rtl_2s_ease-in-out_infinite]'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'swing',
                  class: {
                    thead: 'after:animate-[swing_2s_ease-in-out_infinite]'
                  }
                },
                {
                  loading: true,
                  loadingAnimation: 'elastic',
                  class: {
                    thead: 'after:animate-[elastic_2s_ease-in-out_infinite]'
                  }
                }
              ],
              defaultVariants: {
                loadingColor: 'primary',
                loadingAnimation: 'carousel'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/table.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[SwitchA control that toggles between two states.](/components/switch)[TabsA
set of tab panels that are displayed one at a time.](/components/tabs)


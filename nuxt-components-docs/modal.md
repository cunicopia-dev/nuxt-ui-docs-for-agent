<!-- source: https://ui.nuxt.com/components/modal --> # Modal

[Dialog](https://reka-
ui.com/docs/components/dialog)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Modal.vue)

A dialog window that can be used to display a message or request user input.

## Usage

Use a [Button](/components/button) or any other component in the default slot
of the Modal.

Then, use the `#content` slot to add the content displayed when the Modal is
open.

    
    
    <template>
      <UModal>
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UModal>
    </template>
    

You can also use the `#header`, `#body` and `#footer` slots to customize the
Modal's content.

### Title

Use the `title` prop to set the title of the Modal's header.

title

    
    
    <template>
      <UModal title="Modal with title">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UModal>
    </template>
    

### Description

Use the `description` prop to set the description of the Modal's header.

description

    
    
    <template>
      <UModal
        title="Modal with description"
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
      >
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UModal>
    </template>
    

### Close

Use the `close` prop to customize or hide the close button (with `false`
value) displayed in the Modal's header.

You can pass any property from the [Button](/components/button) component to
customize it.

close.class

    
    
    <template>
      <UModal
        title="Modal with close button"
        :close="{
          color: 'primary',
          variant: 'outline',
          class: 'rounded-full'
        }"
      >
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UModal>
    </template>
    

The close button is not displayed if the `#content` slot is used as it's a
part of the header.

### Close Icon

Use the `close-icon` prop to customize the close button
[Icon](/components/icon). Defaults to `i-lucide-x`.

closeIcon

    
    
    <template>
      <UModal title="Modal with close button" close-icon="i-lucide-arrow-right">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UModal>
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.close` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.close` key.

### Overlay

Use the `overlay` prop to control whether the Modal has an overlay or not.
Defaults to `true`.

overlay

false

    
    
    <template>
      <UModal :overlay="false" title="Modal without overlay">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UModal>
    </template>
    

### Transition

Use the `transition` prop to control whether the Modal is animated or not.
Defaults to `true`.

transition

false

    
    
    <template>
      <UModal :transition="false" title="Modal without transition">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UModal>
    </template>
    

### Fullscreen

Use the `fullscreen` prop to make the Modal fullscreen.

    
    
    <template>
      <UModal fullscreen title="Modal fullscreen">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </UModal>
    </template>
    

## Examples

### Control open state

You can control the open state by using the `default-open` prop or the
`v-model:open` directive.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    
    defineShortcuts({
      o: () => open.value = !open.value
    })
    </script>
    
    <template>
      <UModal v-model:open="open">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="h-48 m-4" />
        </template>
      </UModal>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the Modal by pressing `O`.

This allows you to move the trigger outside of the Modal or remove it
entirely.

### Prevent closing

Set the `dismissible` prop to `false` to prevent the Modal from being closed
when clicking outside of it or pressing escape. A `close:prevent` event will
be emitted when the user tries to close it.

    
    
    <template>
      <UModal :dismissible="false" title="Modal non-dismissible">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
      </UModal>
    </template>
    

### Programmatic usage

You can use the [`useOverlay`](/composables/use-overlay) composable to open a
Modal programatically.

Make sure to wrap your app with the [`App`](/components/app) component which
uses the
[`OverlayProvider`](https://github.com/nuxt/ui/blob/v3/src/runtime/components/OverlayProvider.vue)
component.

First, create a modal component that will be opened programatically:

ModalExample.vue

    
    
    <script setup lang="ts">
    defineProps<{
      count: number
    }>()
    
    const emit = defineEmits<{ close: [boolean] }>()
    </script>
    
    <template>
      <UModal
        :close="{ onClick: () => emit('close', false) }"
        :title="`This modal was opened programmatically ${count} times`"
      >
        <template #footer>
          <div class="flex gap-2">
            <UButton color="neutral" label="Dismiss" @click="emit('close', false)" />
            <UButton label="Success" @click="emit('close', true)" />
          </div>
        </template>
      </UModal>
    </template>
    

We are emitting a `close` event when the modal is closed or dismissed here.
You can emit any data through the `close` event, however, the event must be
emitted in order to capture the return value.

Then, use it in your app:

Open

    
    
    <script setup lang="ts">
    import { LazyModalExample } from '#components'
    
    const count = ref(0)
    
    const toast = useToast()
    const overlay = useOverlay()
    
    const modal = overlay.create(LazyModalExample, {
      props: {
        count: count.value
      }
    })
    
    async function open() {
      const shouldIncrement = await modal.open()
    
      if (shouldIncrement) {
        count.value++
    
        toast.add({
          title: `Success: ${shouldIncrement}`,
          color: 'success',
          id: 'modal-success'
        })
    
        // Update the count
        modal.patch({
          count: count.value
        })
        return
      }
    
      toast.add({
        title: `Dismissed: ${shouldIncrement}`,
        color: 'error',
        id: 'modal-dismiss'
      })
    }
    </script>
    
    <template>
      <UButton label="Open" color="neutral" variant="subtle" @click="open" />
    </template>
    

You can close the modal within the modal component by emitting
`emit('close')`.

### Nested modals

You can nest modals within each other.

Open

    
    
    <script setup lang="ts">
    const first = ref(false)
    const second = ref(false)
    </script>
    
    <template>
      <UModal v-model:open="first" title="First modal" :ui="{ footer: 'justify-end' }">
        <UButton color="neutral" variant="subtle" label="Open" />
    
        <template #footer>
          <UButton label="Close" color="neutral" variant="outline" @click="first = false" />
    
          <UModal v-model:open="second" title="Second modal" :ui="{ footer: 'justify-end' }">
            <UButton label="Open second" color="neutral" />
    
            <template #footer>
              <UButton label="Close" color="neutral" variant="outline" @click="second = false" />
            </template>
          </UModal>
        </template>
      </UModal>
    </template>
    

### With footer slot

Use the `#footer` slot to add content after the Modal's body.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    </script>
    
    <template>
      <UModal v-model:open="open" title="Modal with footer" description="This is useful when you want a form in a Modal." :ui="{ footer: 'justify-end' }">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-48" />
        </template>
    
        <template #footer>
          <UButton label="Cancel" color="neutral" variant="outline" @click="open = false" />
          <UButton label="Submit" color="neutral" />
        </template>
      </UModal>
    </template>
    

### With command palette

You can use a [CommandPalette](/components/command-palette) component inside
the Modal's content.

Search users...

    
    
    <script setup lang="ts">
    const searchTerm = ref('')
    
    const { data: users, status } = await useFetch('https://jsonplaceholder.typicode.com/users', {
      key: 'command-palette-users',
      params: { q: searchTerm },
      transform: (data: { id: number, name: string, email: string }[]) => {
        return data?.map(user => ({ id: user.id, label: user.name, suffix: user.email, avatar: { src: `https://i.pravatar.cc/120?img=${user.id}` } })) || []
      },
      lazy: true
    })
    
    const groups = computed(() => [{
      id: 'users',
      label: searchTerm.value ? `Users matching “${searchTerm.value}”...` : 'Users',
      items: users.value || [],
      ignoreFilter: true
    }])
    </script>
    
    <template>
      <UModal>
        <UButton
          label="Search users..."
          color="neutral"
          variant="subtle"
          icon="i-lucide-search"
        />
    
        <template #content>
          <UCommandPalette
            v-model:search-term="searchTerm"
            :loading="status === 'pending'"
            :groups="groups"
            placeholder="Search users..."
            class="h-80"
          />
        </template>
      </UModal>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`title`| | ` string`  
`description`| | ` string`  
`content`| | ` Omit<DialogContentProps, "asChild" | "as" | "forceMount"> & Partial<EmitsToProps<DialogContentImplEmits>>`The content of the modal.Show properties

  * `disableOutsidePointerEvents?: boolean`When `true`, hover/focus/click interactions will be disabled on elements outside the `DismissableLayer`. Users will need to click twice on outside elements to interact with them: once to close the `DismissableLayer`, and again to trigger the element.
  * `trapFocus?: boolean`When `true`, focus cannot escape the `Content` via keyboard, pointer, or a programmatic focus. Defaults to `false`.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`
  * `onOpenAutoFocus?: ((event: Event) => void)`
  * `onCloseAutoFocus?: ((event: Event) => void)`

  
`overlay`| `true`| `boolean`Render an overlay behind the modal.  
`transition`| `true`| `boolean`Animate the modal when opening or closing.  
`fullscreen`| `false`| `boolean`When `true`, the modal will take up the full
screen.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the modal in a portal.  
`close`| `true`| `boolean | Partial<ButtonProps>`Display a close button to dismiss the modal. `{ size: 'md', color: 'neutral', variant: 'ghost' }`  
`closeIcon`| `appConfig.ui.icons.close`| ` string`The icon displayed in the
close button.  
`dismissible`| `true`| `boolean`When `false`, the modal will not close when
clicking outside or pressing escape.  
`open`| | `boolean`The controlled open state of the dialog. Can be binded as `v-model:open`.  
`defaultOpen`| | `boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.  
`modal`| `true`| `boolean`The modality of the dialog When set to `true`,  
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.  
`ui`| | ` { overlay?: ClassNameValue; content?: ClassNameValue; header?: ClassNameValue; wrapper?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; close?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ open: boolean; }`  
`content`| `{}`  
`header`| `{}`  
`title`| `{}`  
`description`| `{}`  
`close`| `{ ui: { overlay: (props?: Record<string, any> | undefined) => string; content: (props?: Record<string, any> | undefined) => string; header: (props?: Record<string, any> | undefined) => string; ... 5 more ...; close: (props?: Record<...> | undefined) => string; }; }`  
`body`| `{}`  
`footer`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `[value: boolean]`  
`after:leave`| `[]`  
`close:prevent`| `[]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        modal: {
          slots: {
            overlay: 'fixed inset-0 bg-elevated/75',
            content: 'fixed bg-default divide-y divide-default flex flex-col focus:outline-none',
            header: 'flex items-center gap-1.5 p-4 sm:px-6 min-h-16',
            wrapper: '',
            body: 'flex-1 overflow-y-auto p-4 sm:p-6',
            footer: 'flex items-center gap-1.5 p-4 sm:px-6',
            title: 'text-highlighted font-semibold',
            description: 'mt-1 text-muted text-sm',
            close: 'absolute top-4 end-4'
          },
          variants: {
            transition: {
              true: {
                overlay: 'data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]',
                content: 'data-[state=open]:animate-[scale-in_200ms_ease-out] data-[state=closed]:animate-[scale-out_200ms_ease-in]'
              }
            },
            fullscreen: {
              true: {
                content: 'inset-0'
              },
              false: {
                content: 'top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[calc(100vw-2rem)] max-w-lg max-h-[calc(100dvh-2rem)] sm:max-h-[calc(100dvh-4rem)] rounded-lg shadow-lg ring ring-default'
              }
            }
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
            modal: {
              slots: {
                overlay: 'fixed inset-0 bg-elevated/75',
                content: 'fixed bg-default divide-y divide-default flex flex-col focus:outline-none',
                header: 'flex items-center gap-1.5 p-4 sm:px-6 min-h-16',
                wrapper: '',
                body: 'flex-1 overflow-y-auto p-4 sm:p-6',
                footer: 'flex items-center gap-1.5 p-4 sm:px-6',
                title: 'text-highlighted font-semibold',
                description: 'mt-1 text-muted text-sm',
                close: 'absolute top-4 end-4'
              },
              variants: {
                transition: {
                  true: {
                    overlay: 'data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]',
                    content: 'data-[state=open]:animate-[scale-in_200ms_ease-out] data-[state=closed]:animate-[scale-out_200ms_ease-in]'
                  }
                },
                fullscreen: {
                  true: {
                    content: 'inset-0'
                  },
                  false: {
                    content: 'top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[calc(100vw-2rem)] max-w-lg max-h-[calc(100dvh-2rem)] sm:max-h-[calc(100dvh-4rem)] rounded-lg shadow-lg ring ring-default'
                  }
                }
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
            modal: {
              slots: {
                overlay: 'fixed inset-0 bg-elevated/75',
                content: 'fixed bg-default divide-y divide-default flex flex-col focus:outline-none',
                header: 'flex items-center gap-1.5 p-4 sm:px-6 min-h-16',
                wrapper: '',
                body: 'flex-1 overflow-y-auto p-4 sm:p-6',
                footer: 'flex items-center gap-1.5 p-4 sm:px-6',
                title: 'text-highlighted font-semibold',
                description: 'mt-1 text-muted text-sm',
                close: 'absolute top-4 end-4'
              },
              variants: {
                transition: {
                  true: {
                    overlay: 'data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]',
                    content: 'data-[state=open]:animate-[scale-in_200ms_ease-out] data-[state=closed]:animate-[scale-out_200ms_ease-in]'
                  }
                },
                fullscreen: {
                  true: {
                    content: 'inset-0'
                  },
                  false: {
                    content: 'top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[calc(100vw-2rem)] max-w-lg max-h-[calc(100dvh-2rem)] sm:max-h-[calc(100dvh-4rem)] rounded-lg shadow-lg ring ring-default'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[LinkA wrapper around <NuxtLink> with extra
props.](/components/link)[NavigationMenuA list of links that can be displayed
horizontally or vertically.](/components/navigation-menu)

